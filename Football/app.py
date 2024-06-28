import streamlit as st
import pickle
import json
import numpy as np
import path
import sys


dir = path.Path(__file__).abspath()
sys.path.append(dir.parent.parent)

# Path to models
import pathlib
code_dir = pathlib.Path(__file__).parent.resolve()

path_to_model_goals = code_dir / '../models/goals_model.pkl'
path_to_model_yellow = code_dir / '../models/yellow_cards_model.pkl'
path_to_model_market = code_dir / '../models/market_value_model.pkl'
path_to_model_assist = code_dir / '../models/assist_model.pkl'
path_to_model_injury = code_dir / '../models/injury_model.pkl'

# Load the models
with open(path_to_model_goals, 'rb') as file:
    goals_model = pickle.load(file)

with open(path_to_model_yellow, 'rb') as file:
    yellow_cards_model = pickle.load(file)

with open(path_to_model_market, 'rb') as file:
    market_value_model = pickle.load(file)

with open(path_to_model_assist, 'rb') as file:
    assist_model = pickle.load(file)

with open(path_to_model_injury, 'rb') as file:
    injury_model = pickle.load(file)

# Load the scalers
with open('goals_scaler.pkl', 'rb') as file:
    goals_scaler = pickle.load(file)

with open('yellow_cards_scaler.pkl', 'rb') as file:
    yellow_cards_scaler = pickle.load(file)

with open('market_value_scaler.pkl', 'rb') as file:
    market_value_scaler = pickle.load(file)

with open('assist_scaler.pkl', 'rb') as file:
    assist_scaler = pickle.load(file)

# Load the JSON file for categorical feature conversion
with open('categorical_mapping.json', 'r') as file:
    categorical_mapping = json.load(file)

def convert_categorical_features(features, mapping):
    for key, value in features.items():
        if key in mapping:
            features[key] = mapping[key].get(value, value)
    return features

st.title('⚽Player Performance and Market Value Prediction ⚽')

# Sidebar for navigation
st.sidebar.title("Select the Prediction Model")
prediction_type = st.sidebar.selectbox(
    "Choose a prediction model",
    ("Goals Prediction⚽", "Yellow Cards Prediction🟡", "Transfer Market Value Prediction💸", "Assist Prediction🤝", "Injury Prediction🩹")
)

if prediction_type == "Goals Prediction⚽":
    st.header('Goals Prediction⚽')
    features = {
        'Nation': st.selectbox('Nation', categorical_mapping['Nation'].keys()),
        'Squad': st.selectbox('Squad', categorical_mapping['Squad'].keys()),
        'Comp': st.selectbox('Comp', categorical_mapping['Comp'].keys()),
        'Age': st.number_input('Age', min_value=16, max_value=50, step=1),
        'Minutes_Played': st.number_input('Minutes Played', min_value=0.0),
        'Shots': st.number_input('Shots', min_value=0.0),
        'Shots_on_Target': st.number_input('Shots on Target', min_value=0.0),
        'G_per_SoT': st.number_input('Goals per Shot on Target', min_value=0.0),
        'PKatt': st.number_input('Penalty Kicks Attempted', min_value=0.0)
    }
    if st.button('Predict Goals'):
        features = convert_categorical_features(features, categorical_mapping)
        scaled_features = goals_scaler.transform(np.array(list(features.values())).reshape(1, -1))
        prediction = goals_model.predict(scaled_features)
        st.write(f'Predicted Goals: {prediction[0]}')

elif prediction_type == "Yellow Cards Prediction🟡":
    st.header('Yellow Cards Prediction🟡')
    features = {
        'Nation': st.selectbox('Nation', categorical_mapping['Nation'].keys()),
        'Squad': st.selectbox('Squad', categorical_mapping['Squad'].keys()),
        'Comp': st.selectbox('Comp', categorical_mapping['Comp'].keys()),
        'Age': st.number_input('Age', min_value=16, max_value=50, step=1),
        'Minutes_Played': st.number_input('Minutes Played', min_value=0.0),
        'Fouls_Comitted': st.number_input('Fouls Committed', min_value=0.0),
        'Tackles': st.number_input('Tackles', min_value=0.0)
    }
    if st.button('Predict Yellow Cards'):
        features = convert_categorical_features(features, categorical_mapping)
        scaled_features = yellow_cards_scaler.transform(np.array(list(features.values())).reshape(1, -1))
        prediction = yellow_cards_model.predict(scaled_features)
        st.write(f'Predicted Yellow Cards: {prediction[0]}')

elif prediction_type == "Transfer Market Value Prediction💸":
    st.header('Transfer Market Value Prediction💸')
    features = {
        'Nation': st.selectbox('Nation', categorical_mapping['Nation'].keys()),
        'Squad': st.selectbox('Squad', categorical_mapping['Squad'].keys()),
        'Comp': st.selectbox('Comp', categorical_mapping['Comp'].keys()),
        'Age': st.number_input('Age', min_value=16, max_value=50, step=1),
        'Minutes_Played': st.number_input('Minutes Played', min_value=0.0),
        'Goals': st.number_input('Goals', min_value=0.0),
        'PKatt': st.number_input('Penalty Kicks Attempted', min_value=0.0),
        'highest_market_value_in_eur': st.number_input('Highest Market Value in EUR', min_value=0.0)
    }
    if st.button('Predict Market Value'):
        features = convert_categorical_features(features, categorical_mapping)
        scaled_features = market_value_scaler.transform(np.array(list(features.values())).reshape(1, -1))
        prediction = market_value_model.predict(scaled_features)
        st.write(f'Predicted Market Value: {prediction[0]/1000000} M EUR')

elif prediction_type == "Assist Prediction🤝":
    st.header('Assist Prediction🤝')
    features = {
        'Nation': st.selectbox('Nation', categorical_mapping['Nation'].keys()),
        'Squad': st.selectbox('Squad', categorical_mapping['Squad'].keys()),
        'Comp': st.selectbox('Comp', categorical_mapping['Comp'].keys()),
        'Age': st.number_input('Age', min_value=16, max_value=50, step=1),
        'Minutes_Played': st.number_input('Minutes Played', min_value=0.0),
        'GoalCreatingAction': st.number_input('Goal Creating Action', min_value=0.0),
        'Key_Passes': st.number_input('Key Passes', min_value=0.0)
    }
    if st.button('Predict Assists'):
        features = convert_categorical_features(features, categorical_mapping)
        scaled_features = assist_scaler.transform(np.array(list(features.values())).reshape(1, -1))
        prediction = assist_model.predict(scaled_features)
        st.write(f'Predicted Assists: {prediction[0]}')

elif prediction_type == "Injury Prediction🩹":
    st.header('Injury Prediction🩹')
    features = {
        'Player_Age': st.number_input('Player Age', min_value=16, max_value=50, step=1),
        'Player_Weight': st.number_input('Player Weight (kg)', min_value=40.0),
        'Player_Height': st.number_input('Player Height (cm)', min_value=140.0),
        'Previous_Injuries': st.selectbox('Previous Injuries (0 = No;     1 = Yes)', [0, 1]),
        'Training_Intensity': st.number_input('Training Intensity', min_value=0.0),
        'Recovery_Time': st.number_input('Recovery Time (days)', min_value=0)
    }
    if st.button('Predict Injury'):
        prediction = injury_model.predict(np.array(list(features.values())).reshape(1, -1))
        st.write(f'Predicted Injury Probability: {prediction[0]}')


