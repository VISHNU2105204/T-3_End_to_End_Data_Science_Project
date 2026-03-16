from fastapi import FastAPI, HTTPException
import pandas as pd
import numpy as np
from joblib import load
from nba_api.stats.endpoints import leaguegamefinder

app = FastAPI()

model_saved = load('model_nba.joblib')

@app.get("/")
def home():
    return {"message": "NBA Prediction API is running. Go to /docs for the interactive interface."}

def predict_winner(team_home, team_away):
    gamefinder = leaguegamefinder.LeagueGameFinder(date_from_nullable='01/31/2020', league_id_nullable='00')
    games = gamefinder.get_data_frames()[0]
    
    games = games[['TEAM_NAME', 'GAME_ID', 'GAME_DATE', 'MATCHUP', 'WL', 'PLUS_MINUS']]
    games['GAME_DATE'] = pd.to_datetime(games['GAME_DATE'])
  
    if team_home not in games['TEAM_NAME'].values or team_away not in games['TEAM_NAME'].values:
        raise HTTPException(status_code=404, detail="One or both team names not found. Use full names (e.g., 'Golden State Warriors')")
    msk_home = (games['TEAM_NAME'] == team_home)
    games_30_home = games[msk_home].sort_values('GAME_DATE').tail(30)
    home_plus_minus = games_30_home['PLUS_MINUS'].mean()
    
    msk_away = (games['TEAM_NAME'] == team_away)
    games_30_away = games[msk_away].sort_values('GAME_DATE').tail(30)
    away_plus_minus = games_30_away['PLUS_MINUS'].mean()
    
    games_diff = home_plus_minus - away_plus_minus
    
    input_data = np.array([[games_diff]])
    
    predict_home_win = model_saved.predict(input_data)[0]
    predict_winning_probability = model_saved.predict_proba(input_data)[0][1]

    return {
        'team_home': team_home,
        'team_away': team_away,
        'result': "Home Win" if int(predict_home_win) == 1 else "Away Win",
        'win_probability': round(float(predict_winning_probability), 4)
    }
    
@app.get("/predict_nba_home_win/")
def predict_games_results(team_home: str, team_away: str):
    return predict_winner(team_home, team_away)