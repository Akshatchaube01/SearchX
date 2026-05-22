import axios, { AxiosInstance } from 'axios';

const apiURL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

const api: AxiosInstance = axios.create({
  baseURL: apiURL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export interface SearchResult {
  title: string;
  url: string;
  snippet: string;
  score?: number;
}

export interface SearchResponse {
  results: SearchResult[];
  query: string;
  total: number;
  took: number;
}

export const searchAPI = {
  search: async (query: string, page: number = 1, limit: number = 10): Promise<SearchResponse> => {
    try {
      const response = await api.get<SearchResponse>('/search', {
        params: {
          q: query,
          page,
          limit,
        },
      });
      return response.data;
    } catch (error) {
      console.error('Search API error:', error);
      throw error;
    }
  },

  crawl: async (urls: string[]): Promise<{ status: string; message: string }> => {
    try {
      const response = await api.post('/crawl', {
        urls,
      });
      return response.data;
    } catch (error) {
      console.error('Crawl API error:', error);
      throw error;
    }
  },

  health: async (): Promise<{ status: string }> => {
    try {
      const response = await api.get<{ status: string }>('/health');
      return response.data;
    } catch (error) {
      console.error('Health check error:', error);
      throw error;
    }
  },
};

export default api;
