@echo off
echo Starting RAG Chatbot Backend...
cd /d "%~dp0\backend"
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
pause