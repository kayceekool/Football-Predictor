const API_URL =
  process.env.NEXT_PUBLIC_API_URL;

export async function getPredictions() {
  const response = await fetch(
    `${API_URL}/predictions/today`,
    {
      cache: "no-store"
    }
  );

  return response.json();
}