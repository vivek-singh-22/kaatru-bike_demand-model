import streamlit as st
import pandas as pd
import joblib

st.title("Bike Demand Predictor 🚲")

# Input numeric values
real_atemp = st.slider("Feels-like Temperature (°C)", 0.0, 50.0, 25.0)
real_hum = st.slider("Humidity (%)", 0.0, 100.0, 60.0)
real_wind = st.slider("Windspeed (km/h)", 0.0, 67.0, 15.0)
real_temp = st.slider("Temperature (°C)",0.0,50.0,25.0)

# --- Scale the Inputs ---
atemp_scaled = real_atemp / 50.0
hum_scaled = real_hum / 100.0
windspeed_scaled = real_wind / 67.0
temp_scaled = real_temp / 41.0

# Input categorical values
season = st.selectbox("Season", [1, 2, 3, 4])  # e.g. 1=spring, etc.
yr = st.selectbox("Year", [0, 1])  # 0 = 2011, 1 = 2012
mnth = st.selectbox("Month", list(range(1, 13)))
#weekday = st.selectbox("Weekday", list(range(0, 7)))  # 0=Sunday
weathersit = st.selectbox("Weather", [1, 2, 3])
holiday = st.selectbox("Holiday", [0,1, 2, 3])
workingday = st.selectbox("Workingday", [0,1, 2, 3])

# Assemble input in correct column order
input_data = pd.DataFrame([{
    'temp': temp_scaled,
    'atemp': atemp_scaled,
    'hum': hum_scaled,
    'windspeed': windspeed_scaled,
    'season': season,
    'yr': yr,
    'mnth': mnth,
    'holiday': holiday,
    'workingday': workingday,
    #'weekday': weekday,
    'weathersit': weathersit
}])

# Load the model
model = joblib.load('model.pkl')

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Bike Demands: {int(prediction[0])}")