import MatchCard from "../components/MatchCard";
import { getPredictions } from "../lib/api";

export default async function Home() {
  let predictions: any[] = [];
  let errorMessage = "";

  try {
    predictions = await getPredictions();
  } catch (error: any) {
    errorMessage = error?.message || String(error);
  }

  return (
    <main>
      <h1>Football AI Predictions</h1>

      <p>Predictions loaded: {predictions.length}</p>

      {errorMessage && (
        <p>Error: {errorMessage}</p>
      )}

      {predictions.map((prediction: any) => (
        <MatchCard
          key={prediction.match}
          prediction={prediction}
        />
      ))}
    </main>
  );
}