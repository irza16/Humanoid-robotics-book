# RAG Chatbot for Physical AI & Humanoid Robotics Book

## Overview

This project implements a Retrieval-Augmented Generation (RAG) chatbot for the Physical AI & Humanoid Robotics book. The system allows users to ask questions about book content and receive accurate answers with source attribution.

## Features

- **Smart Q&A**: Ask questions about book content and get accurate answers
- **Text Selection**: Select text on the page and ask questions about it
- **Source Attribution**: All answers include links to the original book sections
- **Chat History**: Conversations are saved and accessible across sessions
- **Mobile Responsive**: Works on all device sizes
- **Multi-Agent Architecture**: Specialized agents for different course modules (ROS 2, Simulation, Isaac, VLA)
- **Intelligent Routing**: Automatic question routing to the most appropriate specialized agent
- **Transparency**: API responses include which subagent processed your request

## Architecture

The system consists of:
- **Frontend**: Vanilla JavaScript widget embedded in Docusaurus
- **Backend**: FastAPI server with multi-agent RAG pipeline
- **Multi-Agent System**: Specialized agents for different course modules:
  - **ROS2Expert**: For ROS 2 related queries (Module 1)
  - **SimulationExpert**: For simulation related queries (Module 2)
  - **IsaacExpert**: For Isaac Sim related queries (Module 3)
  - **VLAExpert**: For Vision-Language-Action queries (Module 4)
- **Coordinator Agent**: Intelligent routing based on keyword matching
- **AI Models**: Google Gemini 2.0 Flash via OpenAI SDK
- **Embeddings**: Cohere embed-english-v3.0
- **Vector DB**: Qdrant Cloud
- **Storage**: Neon Postgres for chat history

## Technology Stack

- Python 3.10+
- FastAPI
- OpenAI Agents SDK
- Google Gemini 2.0 Flash (via OpenAI SDK)
- Cohere embeddings
- Qdrant vector database
- Neon Postgres
- JavaScript (frontend widget)
- Docusaurus (integration)

## Setup

### Prerequisites

- Python 3.10+
- pip
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/humanoid-robotics-book.git
cd humanoid-robotics-book
```

2. Install Python dependencies:
```bash
cd chatbot/backend
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys and configuration
```

### Environment Variables

Create a `.env` file in the `chatbot/backend/` directory with the following:

```
GEMINI_API_KEY=your_gemini_api_key
COHERE_API_KEY=your_cohere_api_key
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
NEON_DATABASE_URL=your_neon_database_url
SECRET_KEY=your_secret_key
ALLOWED_ORIGINS=["https://your-domain.com", "http://localhost:3000"]
```

## Usage

### Running the Backend

```bash
cd chatbot/backend
python main.py
```

The API will be available at `http://localhost:8000`

### Frontend Integration

The chatbot widget is automatically integrated into the Docusaurus site through the `src/theme/Root.js` file. No additional setup is needed.

### Content Ingestion

To ingest book content into the vector database:

```bash
cd chatbot/scripts
python ingest.py --sitemap-url https://your-book-site.com/sitemap.xml
```

## API Endpoints

- `GET /health` - Health check
- `POST /chat` - Chat with the bot
- `POST /ingest` - Ingest book content
- `GET /stats` - Usage statistics

## Development

### Backend Development

The backend is located in `chatbot/backend/` and uses FastAPI:

```bash
cd chatbot/backend
uvicorn main:app --reload
```

### Frontend Development

The frontend widget is in `chatbot/frontend/static/chatbot-widget.js`

## Configuration

### RAG Pipeline Settings

In `chatbot/backend/config.py`, you can adjust:

- `max_question_length`: Maximum length of user questions (default: 2000)
- `max_selected_text_length`: Maximum length of selected text (default: 5000)
- `top_k_chunks`: Number of chunks to retrieve (default: 5)
- `llm_model`: LLM model to use (default: gemini-2.5-flash)

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for production deployment instructions.

## API Documentation

See [API.md](API.md) for detailed API documentation.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

[Add your license information here]

## Support

For support, please open an issue in the GitHub repository.