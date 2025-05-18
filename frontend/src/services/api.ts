import axios from 'axios';
import type { CreateUrlResponse } from '../types/url';

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
});

export const urlService = {
  createShortUrl: async (originalUrl: string): Promise<CreateUrlResponse> => {
    const response = await api.post('/urls/', { original_url: originalUrl });
    return response.data;
  },

  getUrlStats: async (shortCode: string): Promise<CreateUrlResponse> => {
    const response = await api.get(`/stats/${shortCode}/`);
    return response.data;
  },
}; 