const WeaknessCard = ({ weaknesses }) => {

  return (
    <div className="bg-red-950 border border-red-800 rounded-2xl p-6 shadow-lg">

      <h2 className="text-2xl font-bold mb-4 text-red-400">
        Repository Weaknesses
      </h2>

      {weaknesses.length === 0 ? (

        <p className="text-green-400">
          No major weaknesses detected.
        </p>

      ) : (

        <ul className="space-y-4">

          {weaknesses.map((weakness, index) => (

            <li
              key={index}
              className="bg-zinc-900 p-4 rounded-xl"
            >
              {weakness}
            </li>

          ))}

        </ul>

      )}

    </div>
  );
};

export default WeaknessCard;