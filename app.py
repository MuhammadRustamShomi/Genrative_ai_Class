import streamlit as st
import requests

# ---- Page Config ----
st.set_page_config(
    page_title="Weather App",
    page_icon="🌤",
    layout="centered"
)

st.title("🌤 Simple Weather App (API Based)")

# ---- City Database ----
cities = {
    "Lahore": (31.5, 74.3),
    "Karachi": (24.9, 67.0),
    "Islamabad": (33.7, 73.1)
}

# ---- User Input ----
city = st.selectbox("Select a City", list(cities.keys()))

# ---- API Function ----
def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    data = response.json()

    temp = data["current_weather"]["temperature"]
    wind = data["current_weather"]["windspeed"]
    code = data["current_weather"]["weathercode"]

    return temp, wind, code

# ---- Button ----
if st.button("Get Weather"):
    lat, lon = cities[city]
    temp, wind, code = get_weather(lat, lon)

    st.success(f"🌍 **City:** {city}")
    st.write(f"🌡 **Temperature:** `{temp}°C`")
    st.write(f"💨 **Wind Speed:** `{wind} km/h`")
    st.write(f"☁ **Weather Code:** `{code}`")

    st.info("Data fetched from Open-Meteo API")
