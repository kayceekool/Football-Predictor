export default function MatchCard(
{
 prediction
}
:any
){

 return (

  <div className="border rounded p-4">

   <h2>{prediction.match}</h2>

   <p>
    Winner:
    {prediction.winner}
   </p>

   <p>
    O2.5:
    {prediction.over25
     ? "YES"
     : "NO"}
   </p>

<p>
 Over 1.5:
 {prediction.over15
   ? "YES"
   : "NO"}
</p>

   <p>
    BTTS:
    {prediction.btts
     ? "YES"
     : "NO"}
   </p>

   <p>
    Score:
    {prediction.score}
   </p>

   <p>
    Confidence:
    {prediction.confidence}%
   </p>

  </div>

 );
}