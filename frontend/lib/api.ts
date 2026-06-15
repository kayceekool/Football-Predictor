const API_URL = process.env.NEXT_PUBLIC_API_URL;

export async function getPredictions() {
  if (!API_URL) {
    throw new Error("NEXT_PUBLIC_API_URL is not configured");
  }

  const response = await fetch(
    `${API_URL}/predictions/today`,
    {
      cache: "no-store",
    }
  );

  if (!response.ok) {
    throw new Error(
      `API error: ${response.status}`
    );
  }

  return response.json();
}