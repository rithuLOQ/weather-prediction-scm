# 🌦 Complete Weather Prediction App (Regression + Classification)
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import r2_score, accuracy_score

# 1️⃣ Sample Weather Dataset
data = {
    "Temperature": [25, 30, 35, 28, 32, 31, 27, 29, 34, 33, 22, 24, 26, 37, 36],
    "Humidity": [80, 65, 55, 70, 60, 75, 85, 68, 50, 58, 90, 82, 77, 45, 48],
    "WindSpeed": [10, 12, 8, 11, 9, 13, 7, 10, 12, 11, 5, 6, 8, 14, 15],
    "Rainfall": [10, 2, 0, 20, 1, 5, 25, 8, 0, 4, 30, 18, 12, 0, 0],
    "Condition": ["Cloudy", "Sunny", "Sunny", "Rainy", "Sunny", "Cloudy", "Rainy",
                  "Cloudy", "Sunny", "Cloudy", "Rainy", "Rainy", "Cloudy", "Sunny", "Sunny"]
}
df = pd.DataFrame(data)

# 2️⃣ Encode 'Condition' for numeric processing
df_encoded = df.copy()
df_encoded["Condition"] = df_encoded["Condition"].astype("category").cat.codes
condition_map = dict(enumerate(df["Condition"].astype("category").cat.categories))

# 3️⃣ Split data for Rainfall prediction (Regression)
X_reg = df_encoded.drop("Rainfall", axis=1)
y_reg = df_encoded["Rainfall"]
Xr_train, Xr_test, yr_train, yr_test = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

# 4️⃣ Split data for Condition prediction (Classification)
X_clf = df_encoded.drop("Condition", axis=1)
y_clf = df_encoded["Condition"]
Xc_train, Xc_test, yc_train, yc_test = train_test_split(X_clf, y_clf, test_size=0.2, random_state=42)

# 5️⃣ Train Regression Models
lr = LinearRegression().fit(Xr_train, yr_train)
dt = DecisionTreeRegressor(random_state=42).fit(Xr_train, yr_train)
rf = RandomForestRegressor(n_estimators=100, random_state=42).fit(Xr_train, yr_train)

# 6️⃣ Train Classification Model
rf_clf = RandomForestClassifier(n_estimators=100, random_state=42).fit(Xc_train, yc_train)

# 7️⃣ Streamlit Interface
st.title("🌦 Weather Prediction App")
st.write("This app predicts **Rainfall (mm)** using regression models and **Weather Condition** using a classifier.")

# 8️⃣ User Inputs
temp = st.slider("🌡️ Temperature (°C)", 0.0, 50.0, 30.0)
humidity = st.slider("💧 Humidity (%)", 0.0, 100.0, 70.0)
windspeed = st.slider("🌬️ Wind Speed (km/h)", 0.0, 30.0, 10.0)
rainfall = st.slider("🌧️ Rainfall (mm)", 0.0, 50.0, 10.0)  # used for classification
st.write("*(Note: Rainfall input is used for predicting weather summary)*")

# 9️⃣ Predict Button
if st.button("🔍 Predict Weather"):
    # Regression Input
    X_input_reg = np.array([[temp, humidity, windspeed, 0]])  # dummy 'Condition' field
    # Classification Input
    X_input_clf = np.array([[temp, humidity, windspeed, rainfall]])

    # 🌧️ Rainfall Predictions
    pred_lr = lr.predict(X_input_reg)[0]
    pred_dt = dt.predict(X_input_reg)[0]
    pred_rf = rf.predict(X_input_reg)[0]

    # 🌤️ Condition Prediction
    pred_cond_code = rf_clf.predict(X_input_clf)[0]
    pred_cond = condition_map[pred_cond_code]

    # Results
    st.subheader("🌧️ Predicted Rainfall (mm):")
    st.write(f"**Linear Regression:** {pred_lr:.2f}")
    st.write(f"**Decision Tree:** {pred_dt:.2f}")
    st.write(f"**Random Forest:** {pred_rf:.2f}")

    st.subheader("🌤️ Predicted Weather Summary:")
    st.success(f"**{pred_cond}**")

    # Performance metrics
    st.markdown("### 📊 Model Performance")
    st.write(f"Linear Regression R²: **{r2_score(yr_test, lr.predict(Xr_test)):.2f}**")
    st.write(f"Decision Tree R²: **{r2_score(yr_test, dt.predict(Xr_test)):.2f}**")
    st.write(f"Random Forest R²: **{r2_score(yr_test, rf.predict(Xr_test)):.2f}**")
    st.write(f"Classification Accuracy: **{accuracy_score(yc_test, rf_clf.predict(Xc_test)):.2f}**")

    # Comparison Chart
    st.markdown("### 📈 Model Comparison (Rainfall Prediction)")
    st.bar_chart({
        "Linear Regression": [pred_lr],
        "Decision Tree": [pred_dt],
        "Random Forest": [pred_rf]
    })
