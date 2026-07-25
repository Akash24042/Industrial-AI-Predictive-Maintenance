import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
data = pd.read_csv("ml/dataset.csv")

# Input features
X = data[
    [
        "temperature",
        "vibration",
        "pressure",
        "rpm",
        "operating_hours"
    ]
]

# Target
y = data["failure"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save model
joblib.dump(model, "ml/predictx_model.pkl")

print("Model saved successfully!")