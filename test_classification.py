# test_classification.py
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

def test_weather_condition_classification():
    # 1. Setup sample data for the automated test
    data = {
        "Temperature": [25, 30, 35, 28],
        "Humidity": [80, 65, 55, 70],
        "WindSpeed": [10, 12, 8, 11],
        "Rainfall": [10, 2, 0, 20],
        "Condition": ["Cloudy", "Sunny", "Sunny", "Rainy"]
    }
    df = pd.DataFrame(data)
    
    # 2. Encode 'Condition' for numeric processing
    df["ConditionCode"] = df["Condition"].astype("category").cat.codes
    condition_map = dict(enumerate(df["Condition"].astype("category").cat.categories))
    
    X_train = df.drop(["Condition", "ConditionCode"], axis=1)
    y_train = df["ConditionCode"]
    
    # 3. Train the model
    rf_clf = RandomForestClassifier(n_estimators=10, random_state=42).fit(X_train, y_train)
    
    # 4. Predict using dummy input (Temp: 27, Humidity: 85, Wind: 7, Rain: 25)
    X_test = np.array([[27, 85, 7, 25]])
    prediction_code = rf_clf.predict(X_test)[0]
    predicted_condition = condition_map[prediction_code]
    
    # 5. SCM Automated Assertions (Ensures the app doesn't break during updates)
    assert predicted_condition in ["Cloudy", "Sunny", "Rainy"], "Prediction is outside expected categories"
    assert isinstance(predicted_condition, str), "Prediction should be a string"
    print(f"Test Passed! 🚀 Predicted Weather Condition: {predicted_condition}")