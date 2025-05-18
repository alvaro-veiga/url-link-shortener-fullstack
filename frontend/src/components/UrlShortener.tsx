import { useState } from 'react';
import {
  Box,
  TextField,
  Button,
  Typography,
  Paper,
  Container,
  Snackbar,
  Alert,
  CircularProgress,
} from '@mui/material';
import ContentCopyIcon from '@mui/icons-material/ContentCopy';
import { urlService } from '../services/api';
import type { CreateUrlResponse } from '../types/url';

export const UrlShortener = () => {
  const [url, setUrl] = useState('');
  const [shortenedUrl, setShortenedUrl] = useState<CreateUrlResponse | null>(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const [snackbar, setSnackbar] = useState({ open: false, message: '', severity: 'success' as 'success' | 'error' });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!url) {
      setError('Por favor, insira uma URL');
      return;
    }

    try {
      setLoading(true);
      setError('');
      const response = await urlService.createShortUrl(url);
      setShortenedUrl(response);
      setSnackbar({
        open: true,
        message: 'URL encurtada com sucesso!',
        severity: 'success',
      });
    } catch (err) {
      setError('Erro ao encurtar URL. Por favor, tente novamente.');
      setSnackbar({
        open: true,
        message: 'Erro ao encurtar URL',
        severity: 'error',
      });
    } finally {
      setLoading(false);
    }
  };

  const copyToClipboard = () => {
    if (shortenedUrl) {
      navigator.clipboard.writeText(shortenedUrl.short_url);
      setSnackbar({
        open: true,
        message: 'URL copiada para a área de transferência!',
        severity: 'success',
      });
    }
  };

  return (
    <Container maxWidth="sm">
      <Box sx={{ mt: 4 }}>
        <Paper elevation={3} sx={{ p: 4 }}>
          <Typography variant="h4" component="h1" gutterBottom align="center" color="primary">
            Encurtador de URL
          </Typography>
          
          <form onSubmit={handleSubmit}>
            <TextField
              fullWidth
              label="Cole sua URL aqui"
              variant="outlined"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              margin="normal"
              error={!!error}
              helperText={error}
              disabled={loading}
            />
            
            <Button
              fullWidth
              variant="contained"
              color="primary"
              type="submit"
              sx={{ mt: 2 }}
              disabled={loading}
            >
              {loading ? <CircularProgress size={24} /> : 'Encurtar URL'}
            </Button>
          </form>

          {shortenedUrl && (
            <Box sx={{ mt: 4 }}>
              <Typography variant="h6" gutterBottom color="primary">
                URL Encurtada:
              </Typography>
              <Paper
                variant="outlined"
                sx={{
                  p: 2,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  backgroundColor: '#f5f5f5',
                  borderRadius: 2,
                }}
              >
                <Typography
                  component="a"
                  href={shortenedUrl.short_url}
                  target="_blank"
                  rel="noopener noreferrer"
                  sx={{
                    textDecoration: 'none',
                    color: 'primary.main',
                    wordBreak: 'break-all',
                    mr: 2,
                  }}
                >
                  {shortenedUrl.short_url}
                </Typography>
                <Button
                  startIcon={<ContentCopyIcon />}
                  onClick={copyToClipboard}
                  size="small"
                  variant="outlined"
                >
                  Copiar
                </Button>
              </Paper>
              
              <Box sx={{ mt: 2 }}>
                <Typography variant="body2" color="text.secondary">
                  Cliques: {shortenedUrl.clicks}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  Criado em: {new Date(shortenedUrl.created_at).toLocaleString()}
                </Typography>
              </Box>
            </Box>
          )}
        </Paper>
      </Box>

      <Snackbar
        open={snackbar.open}
        autoHideDuration={3000}
        onClose={() => setSnackbar({ ...snackbar, open: false })}
      >
        <Alert
          onClose={() => setSnackbar({ ...snackbar, open: false })}
          severity={snackbar.severity}
          sx={{ width: '100%' }}
        >
          {snackbar.message}
        </Alert>
      </Snackbar>
    </Container>
  );
}; 