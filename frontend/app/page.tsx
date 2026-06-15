import MatchCard from "../components/MatchCard";
import { getPredictions } from "../lib/api";

export default async function Home() {
  let predictions = [];

  try {
    predictions = await getPredictions();
  } catch (error) {
    console.error("Prediction fetch error:", error);
  }

  return (
    <main>
      <h1>Football AI Predictions</h1>

      {Array.isArray(predictions) ? (
        predictions.map((prediction: any) => (
          <MatchCard
            key={prediction.match}
            prediction={prediction}
          />
        ))
      ) : (
        <p>No predictions available.</p>
      )}
    </main>
  );
}