const AIReport = ({ report }) => {

  return (
    <div className="bg-white shadow-md rounded-xl p-6">

      <h2 className="text-2xl font-bold mb-4">
        AI Report
      </h2>

      <p className="leading-7 whitespace-pre-line">
        {report}
      </p>

    </div>
  );
};

export default AIReport;