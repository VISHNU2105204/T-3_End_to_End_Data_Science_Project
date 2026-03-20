# Task - 3 
# End-to-End-Data-Science-Project
*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: BADIMELA VISHNU VARDHAN

*INTERN ID*: CTIS1342

*DOMAIN*: DATA SCIENCE

*DURATION*: 12 WEEKS

*MENTOR*: NEELA SANTHOSH

## This is a sophisticated end-to-end data science project that integrates data engineering, machine learning, API development, and web-based visualization to predict the outcome of NBA games. The project follows the full lifecycle of a production-grade data product: from raw data ingestion to a user-facing dashboard.

## The project begins by leveraging the nba_api to fetch historical league data, specifically using the leaguegamefinder endpoint. The dataset covers games from early 2020 through early 2026, providing a robust historical context.

## Using XGBoost, a powerful gradient-boosted decision tree algorithm, you built a binary classifier to predict whether the home team would win or lose. The development process included Data Preparation, Hyperparameter Tuning, Validation, Model Persistence.

## To make the model accessible to other applications, you developed a RESTful API using FastAPI. This layer acts as the "brain" of the operation. When a request is made to the /predict_nba_home_win/ endpoint

## The final layer is a user-facing dashboard built with Plotly Dash. This interface allows non-technical users to interact with the complex backend. Users can select any two NBA teams from dropdown menus, and the dashboard sends a request to the FastAPI backend. It then dynamically displays the predicted winner and the confidence level (probability) of that prediction.

## OUTPUT:
<img width="1911" height="642" alt="Image" src="https://github.com/user-attachments/assets/6ebf438c-9f8e-4219-8197-9b5fabf7545b" />

<img width="1912" height="1026" alt="Image" src="https://github.com/user-attachments/assets/38bd7765-ec0e-475e-adef-2cab97c42b48" />
