export interface ShortenedUrl {
  id: number;
  original_url: string;
  short_code: string;
  short_url: string;
  clicks: number;
  created_at: string;
}

export interface CreateUrlResponse {
    original_url: string;
    short_code: string;
    short_url: string;
    clicks: number;
    created_at: string;
  }