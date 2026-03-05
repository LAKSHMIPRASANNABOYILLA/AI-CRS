import React from 'react';
import { Link } from 'react-router-dom';

function Dashboard({ reviews, loading }) {
  if (loading) return <p>Loading reviews...</p>;
  if (!reviews.length) return <p>No reviews yet. <Link to="/review">Create one!</Link></p>;

  return (
    <table className="reviews-table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Title</th>
          <th>Language</th>
          <th>Status</th>
          <th>Created</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {reviews.map((r) => (
          <tr key={r.id}>
            <td>{r.id}</td>
            <td>{r.title}</td>
            <td>{r.language}</td>
            <td><span className={`status status-${r.status}`}>{r.status}</span></td>
            <td>{new Date(r.created_at).toLocaleDateString()}</td>
            <td><Link to={`/reviews/${r.id}`}>View</Link></td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default Dashboard;
