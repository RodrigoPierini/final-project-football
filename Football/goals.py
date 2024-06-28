# Import necessary libraries
import pandas as pd
import json
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, root_mean_squared_error
import pickle

# Load the dataset
data = pd.read_csv('../Data/archive_football/player_stats_big_5.csv')

# Drop goalkeeper-specific columns as they are not relevant for the analysis
data = data.drop(columns=['Goals_Against_GK','SoT_Against_GK','Saves_GK','Save_percent_GK','Clean_Sheets_GK','CS_percent_GK','PK_Faced_GK','PK_Allowed_GK','PK_Saved_GK','PK_Missed_GK','Save_percent_Penalty_GK','FK_Goals_GK','CornerKick_Goals_GK','OG_GK','PSxG_GK','PSxG_per_SoT_GK','PSxG+_per_minus_GK','LaunchedPassesCompleted_GK','LaunchedAttempted_GK','Cmp_percent_Launched_GK','Att_Passes_GK','Throws_GK','Launch_percent_Passes_GK','AvgLen_Passes_GK','Att_Goal_Kicks_GK','AvgLen_GoalKick_GK','CrossesFaced_GK','CrossedStopped_GK','CrossedStopped_Perc_GK','OPA_Sweeper_GK','OPA_per_90_Sweeper_GK','AvgDist_Sweeper_GK'])

# Filter data for forwards (FW) and players with forward positions
data_fw = data[data['Pos'].isin(['FW', 'MF,FW', 'FW,MF', 'DF,FW', 'FW,DF'])]

# Select relevant columns for machine learning
data_fw_ml = data_fw[['Player', 'Nation', 'Squad', 'Comp', 'Age', 'Minutes_Played', 'Goals', 'Shots', 'Shots_on_Target', 'G_per_SoT', 'FK_Standard', 'PKatt', 'GoalCreatingAction']]

# Create the mapping for 'Nation'
nation_list = data_fw_ml['Nation'].unique()
nation_to_int = {nation: idx for idx, nation in enumerate(nation_list)}
int_to_nation = {idx: nation for nation, idx in nation_to_int.items()}

# Apply the mapping to the DataFrame
data_fw_ml.loc[:,'Nation'] = data_fw_ml['Nation'].map(nation_to_int)

# Save the mapping for future reference
with open('nation_to_int.json', 'w') as f:
    json.dump(nation_to_int, f)
with open('int_to_nation.json', 'w') as f:
    json.dump(int_to_nation, f)

# Create the mapping for 'Squad'
squad_list = data_fw_ml['Squad'].unique()
squad_to_int = {squad: idx for idx, squad in enumerate(squad_list)}
int_to_squad = {idx: squad for squad, idx in squad_to_int.items()}

# Apply the mapping to the DataFrame
data_fw_ml.loc[:,'Squad'] = data_fw_ml['Squad'].map(squad_to_int)

# Save the mapping for future reference
with open('squad_to_int.json', 'w') as f:
    json.dump(squad_to_int, f)
with open('int_to_squad.json', 'w') as f:
    json.dump(int_to_squad, f)

# Replace NaN values with 0 using isna, where, and .loc
data_fw_ml.loc[:, :] = data_fw_ml.where(~data_fw_ml.isna(), 0)

# Create a mapping dictionary for the 'Comp' column
comp_mapping = {
    'Premier League': 0,
    'Ligue 1': 1,
    'Serie A': 2,
    'Bundesliga': 3,
    'La Liga': 4
}

# Apply the mapping to the 'Comp' column
data_fw_ml.loc[:,'Comp'] = data_fw_ml['Comp'].map(comp_mapping)

# Prepare features (X) and target (y)
X = data_fw_ml.drop(columns=['Goals', 'Player', 'FK_Standard', 'GoalCreatingAction'])
y = data_fw_ml['Goals']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize and train the model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Calculate evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = root_mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the evaluation metrics
print(f'MAE: {mae}')
print(f'MSE: {mse}')
print(f'RMSE: {rmse}')
print(f'R2: {r2}')


# Save the model
pickle.dump(model, open("goals_model.pkl", "wb"))

# Save the scaler
pickle.dump(scaler, open("goals_scaler.pkl", "wb"))