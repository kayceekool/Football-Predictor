const API_URL =
process.env.NEXT_PUBLIC_API_URL;

export async function getPredictions() {

  const res =
  await fetch(
      `${API_URL}/predictions/today`
  );

  return res.json();
}