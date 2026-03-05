import React from 'react';
import { Link } from 'react-router-dom';

function HomePage() {
  return (
    <div className="home-page">
      <h1>AI Code Review System</h1>
      <p>Submit your code and get instant AI-powered feedback.</p>
      <div className="actions">
        <Link to="/review" className="btn btn-primary">New Review</Link>
        <Link to="/dashboard" className="btn btn-secondary">Dashboard</Link>
      </div>
    </div>
  );
}

export default HomePage;
