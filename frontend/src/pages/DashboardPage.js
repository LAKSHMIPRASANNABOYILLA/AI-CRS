import React, { useEffect, useState } from 'react';
import Dashboard from '../components/Dashboard/Dashboard';
import { reviewService } from '../services/reviewService';

function DashboardPage() {
  const [reviews, setReviews] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    reviewService.listReviews()
      .then(setReviews)
      .catch(console.error)
      .finally(() => setLoading(false));
  }, []);

  return (
    <div className="dashboard-page">
      <h2>Review Dashboard</h2>
      <Dashboard reviews={reviews} loading={loading} />
    </div>
  );
}

export default DashboardPage;
