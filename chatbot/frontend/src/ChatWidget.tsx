import React, { useState, useEffect } from 'react';
import { apiClient, ChatResponse } from './api';

interface Message {
  id: string;
  type: 'user' | 'assistant';
  content: string;
  sources?: Array<{
    url: string;
    title: string;
    content: string;
  }>;
  timestamp: Date;
}

const ChatWidget: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState<Message[]>(() => {
    // Load messages from localStorage if available
    const savedMessages = localStorage.getItem('chatMessages');
    return savedMessages ? JSON.parse(savedMessages) : [];
  });
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [sessionId, setSessionId] = useState<string | null>(() => {
    // Load session ID from localStorage if available
    return localStorage.getItem('chatSessionId');
  });
  const [selectedText, setSelectedText] = useState<string | null>(null);

  // Check for selected text when the component mounts
  useEffect(() => {
    const handleSelection = () => {
      const text = window.getSelection()?.toString().trim();
      if (text) {
        setSelectedText(text);
      } else {
        setSelectedText(null);
      }
    };

    // Add event listeners for text selection
    document.addEventListener('mouseup', handleSelection);
    document.addEventListener('keyup', handleSelection);

    // Cleanup event listeners
    return () => {
      document.removeEventListener('mouseup', handleSelection);
      document.removeEventListener('keyup', handleSelection);
    };
  }, []);

  // Save messages to localStorage whenever messages change
  useEffect(() => {
    localStorage.setItem('chatMessages', JSON.stringify(messages));
  }, [messages]);

  // Save session ID to localStorage whenever it changes
  useEffect(() => {
    if (sessionId) {
      localStorage.setItem('chatSessionId', sessionId);
    } else {
      localStorage.removeItem('chatSessionId');
    }
  }, [sessionId]);

  const toggleChat = () => {
    setIsOpen(!isOpen);
  };

  const handleSendMessage = async () => {
    if (!inputValue.trim() || isLoading) return;

    // Add user message
    const userMessage: Message = {
      id: Date.now().toString(),
      type: 'user',
      content: inputValue,
      timestamp: new Date(),
    };

    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);

    try {
      // Call the backend API with selected text if available
      const response: ChatResponse = await apiClient.chat({
        question: inputValue,
        selected_text: selectedText || undefined,
        session_id: sessionId || undefined,
      });

      // Update session ID if it was returned
      if (response.session_id && !sessionId) {
        setSessionId(response.session_id);
      }

      const assistantMessage: Message = {
        id: (Date.now() + 1).toString(),
        type: 'assistant',
        content: response.answer,
        sources: response.sources,
        timestamp: new Date(),
      };

      setMessages(prev => [...prev, assistantMessage]);

      // Clear selected text after sending the message
      setSelectedText(null);
    } catch (error) {
      console.error('Error sending message:', error);

      // Show error message to user
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        type: 'assistant',
        content: 'Sorry, I encountered an error processing your question. Please try again.',
        timestamp: new Date(),
      };

      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  return (
    <div className="chat-widget">
      {isOpen ? (
        <div className="chat-container">
          <div className="chat-header">
            <h3>Book Assistant</h3>
            <button onClick={toggleChat} className="close-btn">X</button>
          </div>

          <div className="chat-messages">
            {messages.map((message) => (
              <div
                key={message.id}
                className={`message ${message.type}`}
              >
                <div className="message-content">{message.content}</div>
                {message.sources && message.sources.length > 0 && (
                  <div className="sources">
                    <strong>Sources:</strong>
                    {message.sources.map((source, idx) => (
                      <div key={idx} className="source">
                        <a href={source.url} target="_blank" rel="noopener noreferrer">
                          {source.title}
                        </a>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            ))}

            {isLoading && (
              <div className="message assistant">
                <div className="message-content">Thinking...</div>
              </div>
            )}
          </div>

          <div className="chat-input-area">
            <textarea
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Ask a question about the book..."
              disabled={isLoading}
            />
            <button
              onClick={handleSendMessage}
              disabled={isLoading || !inputValue.trim()}
              className="send-btn"
            >
              Send
            </button>
          </div>
        </div>
      ) : (
        <button onClick={toggleChat} className="chat-toggle">
          💬 Ask Book Questions
        </button>
      )}

      <style jsx>{`
        .chat-widget {
          position: fixed;
          bottom: 20px;
          right: 20px;
          z-index: 10000;
        }

        .chat-toggle {
          background-color: #4f46e5;
          color: white;
          border: none;
          border-radius: 50%;
          width: 60px;
          height: 60px;
          font-size: 24px;
          cursor: pointer;
          box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .chat-container {
          width: 350px;
          height: 500px;
          border: 1px solid #e5e7eb;
          border-radius: 8px;
          display: flex;
          flex-direction: column;
          background: white;
          box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
          overflow: hidden;
        }

        .chat-header {
          background-color: #4f46e5;
          color: white;
          padding: 12px;
          display: flex;
          justify-content: space-between;
          align-items: center;
        }

        .close-btn {
          background: none;
          border: none;
          color: white;
          font-size: 18px;
          cursor: pointer;
        }

        .chat-messages {
          flex: 1;
          overflow-y: auto;
          padding: 12px;
          display: flex;
          flex-direction: column;
          gap: 12px;
        }

        .message {
          max-width: 80%;
          padding: 8px 12px;
          border-radius: 8px;
          word-wrap: break-word;
        }

        .message.user {
          align-self: flex-end;
          background-color: #dbeafe;
          border-bottom-right-radius: 2px;
        }

        .message.assistant {
          align-self: flex-start;
          background-color: #f3f4f6;
          border-bottom-left-radius: 2px;
        }

        .sources {
          margin-top: 8px;
          padding-top: 8px;
          border-top: 1px solid #e5e7eb;
          font-size: 12px;
        }

        .source {
          margin: 4px 0;
        }

        .source a {
          color: #4f46e5;
          text-decoration: none;
        }

        .source a:hover {
          text-decoration: underline;
        }

        .chat-input-area {
          padding: 12px;
          border-top: 1px solid #e5e7eb;
          display: flex;
          flex-direction: column;
        }

        textarea {
          width: 100%;
          min-height: 60px;
          padding: 8px;
          border: 1px solid #e5e7eb;
          border-radius: 4px;
          resize: vertical;
          margin-bottom: 8px;
        }

        .send-btn {
          align-self: flex-end;
          background-color: #4f46e5;
          color: white;
          border: none;
          padding: 8px 16px;
          border-radius: 4px;
          cursor: pointer;
        }

        .send-btn:disabled {
          background-color: #9ca3af;
          cursor: not-allowed;
        }
      `}</style>
    </div>
  );
};

export default ChatWidget;