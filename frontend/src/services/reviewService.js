import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1';

const api = axios.create({ baseURL: API_URL });

export const reviewService = {
  createReview: (data) => api.post('/reviews', data).then((r) => r.data),
  listReviews: (skip = 0, limit = 20) =>
    api.get('/reviews', { params: { skip, limit } }).then((r) => r.data),
  getReview: (id) => api.get(`/reviews/${id}`).then((r) => r.data),
};
