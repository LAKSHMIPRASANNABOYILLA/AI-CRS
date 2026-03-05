import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import CodeEditor from '../components/CodeEditor/CodeEditor';
import ReviewPanel from '../components/ReviewPanel/ReviewPanel';
import { reviewService } from '../services/reviewService';
import { useReview } from '../hooks/useReview';

function ReviewPage() {
  const { id } = useParams();
  const { review: existingReview } = useReview(id);
  const [newReview, setNewReview] = useState(null);
  const [loading, setLoading] = useState(false);

  const review = existingReview || newReview;

  const handleSubmit = async (title, language, code) => {
    setLoading(true);
    try {
      const result = await reviewService.createReview({ title, language, code_snippet: code });
      setNewReview(result);
    } catch (error) {
      console.error('Review failed:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="review-page">
      <h2>Code Review</h2>
      {!id && <CodeEditor onSubmit={handleSubmit} loading={loading} />}
      {review && <ReviewPanel review={review} />}
    </div>
  );
}

export default ReviewPage;
