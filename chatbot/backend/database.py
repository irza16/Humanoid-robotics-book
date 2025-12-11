from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, ForeignKey, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from retry_utils import retry_with_backoff


# Pydantic models for request/response validation
class ChatSessionBase(BaseModel):
    user_id: Optional[str] = None


class ChatSessionCreate(ChatSessionBase):
    pass


class ChatSession(ChatSessionBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ChatMessageBase(BaseModel):
    session_id: int
    question: str
    answer: str
    selected_text: Optional[str] = None
    sources: Optional[List[str]] = []


class ChatMessageCreate(ChatMessageBase):
    pass


class ChatMessage(ChatMessageBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# Database connection and session management
class DatabaseManager:
    def __init__(self, database_url: str):
        self.database_url = database_url
        self.engine = create_engine(database_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_db_session(self):
        """Get a database session"""
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def connect(self):
        """Establish a connection to the database"""
        return psycopg2.connect(self.database_url, cursor_factory=RealDictCursor)

    def create_tables(self):
        """Create required tables if they don't exist"""
        with self.connect() as conn:
            with conn.cursor() as cursor:
                # Create chat_sessions table
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS chat_sessions (
                        id SERIAL PRIMARY KEY,
                        user_id TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """)

                # Create chat_messages table
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS chat_messages (
                        id SERIAL PRIMARY KEY,
                        session_id INTEGER REFERENCES chat_sessions(id),
                        question TEXT NOT NULL,
                        answer TEXT NOT NULL,
                        selected_text TEXT,
                        sources TEXT[],
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """)

                # Create indexes for better performance
                cursor.execute("""
                    CREATE INDEX IF NOT EXISTS idx_session_messages ON chat_messages(session_id);
                """)

                cursor.execute("""
                    CREATE INDEX IF NOT EXISTS idx_created_at ON chat_messages(created_at);
                """)

                conn.commit()

    @retry_with_backoff(
        max_retries=3,
        base_delay=0.5,
        max_delay=10.0,
        exceptions=(psycopg2.OperationalError, psycopg2.InterfaceError)
    )
    def create_session(self, user_id: Optional[str] = None) -> int:
        """Create a new chat session and return its ID"""
        with self.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO chat_sessions (user_id) VALUES (%s) RETURNING id",
                    (user_id,)
                )
                session_id = cursor.fetchone()[0]
                conn.commit()
                return session_id

    @retry_with_backoff(
        max_retries=3,
        base_delay=0.5,
        max_delay=10.0,
        exceptions=(psycopg2.OperationalError, psycopg2.InterfaceError)
    )
    def add_message(self, session_id: int, question: str, answer: str, selected_text: Optional[str] = None, sources: Optional[List[str]] = None) -> int:
        """Add a new message to a session"""
        if sources is None:
            sources = []

        with self.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO chat_messages (session_id, question, answer, selected_text, sources)
                    VALUES (%s, %s, %s, %s, %s) RETURNING id
                    """,
                    (session_id, question, answer, selected_text, sources)
                )
                message_id = cursor.fetchone()[0]
                conn.commit()
                return message_id

    def get_session_messages(self, session_id: int) -> List[dict]:
        """Get all messages for a specific session"""
        with self.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id, session_id, question, answer, selected_text, sources, created_at
                    FROM chat_messages
                    WHERE session_id = %s
                    ORDER BY created_at ASC
                    """,
                    (session_id,)
                )
                return [dict(row) for row in cursor.fetchall()]

    def get_session_by_id(self, session_id: int) -> Optional[dict]:
        """Get a specific session by ID"""
        with self.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id, user_id, created_at
                    FROM chat_sessions
                    WHERE id = %s
                    """,
                    (session_id,)
                )
                result = cursor.fetchone()
                return dict(result) if result else None

    def get_all_sessions(self) -> List[dict]:
        """Get all chat sessions"""
        with self.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id, user_id, created_at
                    FROM chat_sessions
                    ORDER BY created_at DESC
                    """
                )
                return [dict(row) for row in cursor.fetchall()]


# Global database manager instance
db_manager = None


def init_db_manager(database_url: str):
    """Initialize the database manager"""
    global db_manager
    db_manager = DatabaseManager(database_url)
    db_manager.create_tables()


def get_db_manager() -> DatabaseManager:
    """Get the database manager instance"""
    global db_manager
    if db_manager is None:
        raise RuntimeError("Database manager not initialized")
    return db_manager