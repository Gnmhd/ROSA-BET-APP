const API_KEY = 'COLLE_TA_CLE_THE_ODDS_ICI';
async function loadMatches(){
  const res = await fetch(`https://api.the-odds-api.com/v4/sports/soccer_epl/odds/?apiKey=${API_KEY}&regions=eu&markets=h2h`);
  const data = await res.json();
  console.log(data);
}
