// API client for the RAG Chatbot backend

interface ChatRequest {
  question: string;
  selected_text?: string;
  session_id?: string;
}

interface Source {
  url: string;
  title: string;
  content: string;
}

interface ChatResponse {
  answer: string;
  sources: Source[];
  session_id: string;
}

class ApiClient {
  private baseUrl: string;

  constructor() {
    // Use environment-specific base URL
    this.baseUrl = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000';
  }

  async chat(request: ChatRequest): Promise<ChatResponse> {
    try {
      const response = await fetch(`${this.baseUrl}/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(request),
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.message || `HTTP error! status: ${response.status}`);
      }

      const data: ChatResponse = await response.json();
      return data;
    } catch (error) {
      console.error('Error in chat API call:', error);
      throw error;
    }
  }

  async health(): Promise<{ status: string; timestamp: string; version: string }> {
    try {
      const response = await fetch(`${this.baseUrl}/health`);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return await response.json();
    } catch (error) {
      console.error('Error in health check:', error);
      throw error;
    }
  }
}

export const apiClient = new ApiClient();
export type { ChatRequest, ChatResponse, Source };