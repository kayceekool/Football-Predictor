import MatchCard from "../components/MatchCard";
import { getPredictions } from "../lib/api";

export default async function Home() {
  let predictions: any[] = [];

  try {
    predictions = await getPredictions();
    console.log(predictions);
  } catch (error) {
    return (
      <main>
        <h1>Football AI Predictions</h1>
        <p>Error loading predictions.</p>
        <pre>{String(error)}</pre>
      </main>
    );
  }

  return (
    <main>
      <h1>Football AI Predictions</h1>

      <p>Predictions loaded: {predictions.length}</p>

      {predictions.map((prediction: any) => (
        <MatchCard
          key={prediction.match}
          prediction={prediction}
        />
      ))}
    </main>
  );
}