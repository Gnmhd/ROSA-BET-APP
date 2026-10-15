import random
# ROSA-BET AI ENGINE V1 - Clone AI ScoreCast Logic
def predict_match(home_stats, away_stats, cote_home):
    # Exemple avec AZ Alkmaar vs Hapoel
    xG_home = home_stats.get('xg', 1.8)
    xG_away = away_stats.get('xg', 0.9)
    
    # Probabilités 1X2 comme dans ta vidéo
    prob_home = max(10, min(85, 70 - (float(cote_home)-1)*20 + (xG_home - xG_away)*10))
    prob_draw = 18.4
    prob_away = 100 - prob_home - prob_draw
    
    # Score exact
    if prob_home > 60: score = "2 - 0"
    elif prob_home > 50: score = "2 - 1"
    elif prob_away > 50: score = "0 - 1"
    else: score = "1 - 1"
    
    # Confiance
    signals = 0
    if xG_home > 1.5: signals+=1
    if home_stats.get('form',0) > 3: signals+=1
    if float(cote_home) < 2.0: signals+=1
    
    confiance = "Faible" if signals==1 else "Moyenne" if signals==2 else "Forte"
    stars = "★"*signals
    
    return {
        "resultat": {"1": prob_home, "X": prob_draw, "2": prob_away},
        "score_exact": score,
        "double_chance": "1X" if prob_home>50 else "X2",
        "btts": "OUI" if xG_home>1 and xG_away>0.8 else "NON",
        "over_2_5": "OUI" if xG_home+xG_away>2.5 else "NON",
        "confiance": confiance,
        "stars": stars,
        "detail_frappant": f"{signals} signaux affectent la confiance" if signals>=2 else "",
        "constat": "L'IA a détecté un signal fort à domicile" if prob_home>60 else "Match équilibré"
    }
