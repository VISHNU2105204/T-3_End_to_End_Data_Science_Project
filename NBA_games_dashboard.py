import dash
from dash import dcc, html  # Modern Dash 2.0+ imports
from dash.dependencies import Input, Output
from nba_api.stats.endpoints import leaguegamefinder
import requests

gamefinder = leaguegamefinder.LeagueGameFinder(
    date_from_nullable='05/01/2021', league_id_nullable='00')
games = gamefinder.get_data_frames()[0]

team_names = games['TEAM_NAME'].unique()
team_names.sort()
team_name_dropdown_options = [{'label': i, 'value': i} for i in team_names]

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Welcome to the NBA games winner prediction"),
    html.H2("Home Team"),
    dcc.Dropdown(
        id='home_team',
        options=team_name_dropdown_options,
        value=team_names[0]
    ),
    html.H2("Away Team"),
    dcc.Dropdown(
        id='away_team',
        options=team_name_dropdown_options,
        value=team_names[1]
    ),
    html.H3(id='output_text')
])

@app.callback(
    Output('output_text', 'children'),
    Input('home_team', 'value'),
    Input('away_team', 'value'),
)
def update_output_div(home_team, away_team):
    try:
        response = requests.get(
            'http://127.0.0.1:8000/predict_nba_home_win/', 
            params={'team_home': home_team, 'team_away': away_team},
        )
        response.raise_for_status() 
        json_response = response.json()
        
        if json_response['result'] == "Home Win":
            winning_team = home_team
            probability = json_response['win_probability']
        else:
            winning_team = away_team
            probability = 1 - json_response['win_probability']

        return f'{winning_team} is predicted to win with a probability of {probability:.1%}'
    
    except Exception as e:
        return f"Connection Error: Ensure FastAPI is running at http://127.0.0.1:8000 (Details: {e})"

if __name__ == '__main__':
    app.run(debug=True)