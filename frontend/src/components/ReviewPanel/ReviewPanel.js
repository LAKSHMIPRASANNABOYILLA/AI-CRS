import React from 'react';

const SEVERITY_COLORS = {
  info: '#3498db',
  warning: '#f39c12',
  error: '#e74c3c',
  critical: '#8e44ad',
};

function ReviewPanel({ review }) {
  return (
    <div className="review-panel">
      <h3>Review Result — <span className={`status status-${review.status}`}>{review.status}</span></h3>
      {review.result && <p className="summary">{review.result}</p>}
      {review.comments && review.comments.length > 0 && (
        <ul className="comments-list">
          {review.comments.map((comment, idx) => (
            <li key={idx} style={{ borderLeftColor: SEVERITY_COLORS[comment.severity] }}>
              {comment.line_number && <span className="line">Line {comment.line_number}: </span>}
              <span className={`badge badge-${comment.severity}`}>{comment.severity}</span>
              <p>{comment.message}</p>
              {comment.suggestion && <p className="suggestion">💡 {comment.suggestion}</p>}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default ReviewPanel;
