export interface Prediction {

  match: string;

  winner: string;

  winner_probability: number;

  over25: boolean;

  over25_probability: number;

  btts: boolean;

  btts_probability: number;

  score: string;

  confidence: number;
}