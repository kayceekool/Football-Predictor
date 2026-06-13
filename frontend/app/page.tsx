import MatchCard from "../components/MatchCard";
import { getPredictions } from "../lib/api";

export default async function Home() {
  const predictions = await getPredictions();

  return (
    <main>
      <h1>Football AI Predictions</h1>

      {predictions.map((prediction: any) => (
        <MatchCard
          key={prediction.match}
          prediction={prediction}
        />
      ))}
    </main>
  );
}