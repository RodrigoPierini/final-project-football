# Player Performance and Market Value Prediction App

Welcome to the Player Performance and Market Value Prediction App! This app allows you to predict various aspects of a football player's performance and market value using machine learning models. Below is a comprehensive guide on how to use the app.

## Table of Contents
1. [Overview](#overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Features](#features)
    - [Goals Prediction](#goals-prediction)
    - [Yellow Cards Prediction](#yellow-cards-prediction)
    - [Transfer Market Value Prediction](#transfer-market-value-prediction)
    - [Assist Prediction](#assist-prediction)
    - [Injury Prediction](#injury-prediction)
5. [Contributing](#contributing)

## Overview
This app uses pre-trained machine learning models to predict:
- Goals scored by a player
- Yellow cards received by a player
- Transfer market value of a player
- Assists made by a player
- Probability of a player getting injured

## Installation
To run this app locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/PlayerPerformancePrediction.git
    cd PlayerPerformancePrediction
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the codes:

  `goals.py`, `yellow.py`, `market.py`, `assist.py`, `injury.py`, `mapping.py`
 
  So you will have the necessary model files (`goals_model.pkl`, `yellow_cards_model.pkl`, `market_value_model.pkl`, `assist_model.pkl`, `injury_model.pkl`) and the `categorical_mapping.json` file in the project directory.


4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Usage
Once the app is running, you can navigate through different prediction models using the sidebar. Select the desired prediction type and input the necessary features to get the prediction.

## Features

### Goals Prediction
Predict the number of goals a player will score based on:
- Nation
- Squad
- Competition
- Age
- Minutes Played
- Shots
- Shots on Target
- Goals per Shot on Target
- Penalty Kicks Attempted

### Yellow Cards Prediction
Predict the number of yellow cards a player will receive based on:
- Nation
- Squad
- Competition
- Age
- Minutes Played
- Fouls Committed
- Tackles

### Transfer Market Value Prediction
Predict the transfer market value of a player based on:
- Nation
- Squad
- Competition
- Age
- Minutes Played
- Goals
- Penalty Kicks Attempted
- Highest Market Value in EUR

### Assist Prediction
Predict the number of assists a player will make based on:
- Nation
- Squad
- Competition
- Age
- Minutes Played
- Goal Creating Actions
- Key Passes

### Injury Prediction
Predict the probability of a player getting injured based on:
- Player Age
- Player Weight
- Player Height
- Previous Injuries
- Training Intensity
- Recovery Time

## Contributing
We welcome contributions to enhance the functionality and usability of this app. Please feel free to fork the repository, make changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.
