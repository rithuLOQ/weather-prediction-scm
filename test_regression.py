# test_regression.py
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def test_rainfall_regression_model():
    # 1. Setup sample data for the automated test
    data = {
        "Temperature": [25, 30, 35, 28],
        "Humidity": [80, 65, 55, 70],
        "WindSpeed": [10, 12, 8, 11],
        "Rainfall": [10, 2, 0, 20]
    }
    df = pd.DataFrame(data)
    
    X_train = df.drop("Rainfall", axis=1)
    y_train = df["Rainfall"]
    
    # 2. Train the model
    model = LinearRegression().fit(X_train, y_train)
    
    # 3. Predict using dummy input (Temp: 32, Humidity: 60, Wind: 9)
    X_test = np.array([[32, 60, 9]])
    prediction = model.predict(X_test)[0]
    
    # 4. SCM Automated Assertions (If these fail, Jenkins will block the deployment)
    assert prediction is not None, "Model failed to return a prediction"
    assert isinstance(prediction, (float, np.floating)), "Prediction should be a float value"
    print(f"Test Passed! 🚀 Predicted Rainfall: {prediction:.2f} mm")