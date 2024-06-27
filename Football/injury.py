# Import necessary libraries
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, accuracy_score
import pickle

# Load the dataset
data = pd.read_csv('../Data/archive_injuries/injury_data.csv')

X = data.drop(columns=['Likelihood_of_Injury'])
y = data['Likelihood_of_Injury']


# Define models to include in the pipeline
models = [
    ('Logistic Regression', LogisticRegression()),
    ('Random Forest', RandomForestClassifier(n_estimators=100, random_state=42)),
    ('SVM', SVC(kernel='linear', random_state=42)),
    ('Neural Network', MLPClassifier(hidden_layer_sizes=(50, 50), max_iter=500, random_state=42))
]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline for each model
pipelines = []
for name, model in models:
    if name == 'Neural Network':
        pipeline = Pipeline([
            ('scaler', StandardScaler()),  # Scale features for MLP
            (name, model)
        ])
    else:
        pipeline = Pipeline([
            (name, model)
        ])
    pipelines.append((name, pipeline))

# Fit the pipelines and evaluate
for name, pipeline in pipelines:
    print(f"Training {name}...")
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    print(f"Evaluating {name}...")
    print(classification_report(y_test, y_pred))
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("-------------------------")

# Save the model
pickle.dump(model, open("injury_model.pkl", "wb"))