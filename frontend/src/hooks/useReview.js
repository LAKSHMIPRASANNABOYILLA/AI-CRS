import { useState, useEffect } from 'react';
import { reviewService } from '../services/reviewService';

export function useReview(reviewId) {
  const [review, setReview] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!reviewId) return;
    reviewService.getReview(reviewId)
      .then(setReview)
      .catch(setError)
      .finally(() => setLoading(false));
  }, [reviewId]);

  return { review, loading, error };
}
