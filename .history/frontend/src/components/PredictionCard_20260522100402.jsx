const PredictionCard = ({ prediction }) => {

  return (
    <div className="bg-white shadow-md rounded-xl p-6">

      <h2 className="text-2xl font-bold mb-4">
        ML Prediction
      </h2>

      <p>
        {prediction.prediction}
      </p>

      <p className="mt-2">
        <strong>Score:</strong>
        {" "}
        {prediction.score}
      </p>

    </div>
  );
};

export default PredictionCard;