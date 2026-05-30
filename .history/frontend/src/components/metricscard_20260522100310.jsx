const MetricsCard = ({ metrics }) => {

  return (
    <div className="bg-white shadow-md rounded-xl p-6">

      <h2 className="text-2xl font-bold mb-4">
        Metrics
      </h2>

      <p>
        <strong>Popularity Score:</strong>
        {" "}
        {metrics.popularity_score}
      </p>

      <p>
        <strong>Risk Level:</strong>
        {" "}
        {metrics.risk_level}
      </p>

    </div>
  );
};

export default MetricsCard;