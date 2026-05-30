const PredictionCard = ({ prediction }) => {

  return (
    <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6 shadow-lg">

      <h2 className="text-2xl font-bold mb-4 text-cyan-400">
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