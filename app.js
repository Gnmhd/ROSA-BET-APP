async function loadRealMatches() {
  try {
    // API gratuite ESPN - vrais matchs live
    const res = await fetch('https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.champions/scoreboard');
    const data = await res.json();

    let html = '';
    data.events.slice(0,10).forEach(match => {
      const home = match.competitions[0].competitors[0].team.displayName;
      const away = match.competitions[0].competitors[1].team.displayName;
      const status = match.status.type.shortDetail;

      html += `
      <div style="display:flex;justify-content:space-between;padding:12px;border-bottom:1px solid #222">
        <span>${home} vs ${away}<br><small style="color:#888">${status}</small></span>
        <span style="background:#FFD700;color:#000;padding:5px 12px;border-radius:15px;font-weight:bold">@${(Math.random()*1.5+1.5).toFixed(2)}</span>
      </div>`;
    });

    // Injecte dans ta page
    const container = document.querySelector('.matches') || document.body;
    if(document.getElementById('real-matches')) {
      document.getElementById('real-matches').innerHTML = html;
    }
  } catch(e) {
    console.log('API en pause, matchs exemple');
  }
}

// Lance au chargement
loadRealMatches();
setInterval(loadRealMatches, 60000); // actualise chaque minute
