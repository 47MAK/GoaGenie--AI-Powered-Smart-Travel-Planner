import streamlit as st
from weather_api import get_weather
from itinerary import generate_itinerary
from maps_api import extract_places, get_map_link

# Page configuration
st.set_page_config(page_title="GoaGenie", page_icon="🌴", layout="wide")


st.title("🌴 GoaGenie")
st.subheader("AI Travel Planner for Goa")

# ---------------- WEATHER ---------------- #

weather = get_weather()

st.subheader("🌤 Current Weather in Goa")
st.write(weather)

# ---------------- USER INPUTS ---------------- #

st.header("Enter Trip Details")

people = st.number_input("Number of People", 1, 20, 2)

days = st.slider("Trip Duration (Days)", 1, 7, 3)

budget = st.selectbox(
    "Budget per person per day",
    [
        "Low (₹1000–₹2500)",
        "Medium (₹2500–₹6000)",
        "Luxury (₹6000–₹15000+)"
    ]
)

food_pref = st.selectbox(
    "Food Preference",
    ["Vegetarian Only", "Non-Vegetarian", "Both"]
)

st.subheader("Children Age Groups")

kids_0_5 = st.checkbox("Age 0–5")
kids_6_10 = st.checkbox("Age 6–10")

elders = st.checkbox("Traveling with Elders (60+)")

interests = st.multiselect(
    "Select Interests",
    [
        "Beaches",
        "Adventure",
        "Nature",
        "Nightlife",
        "Food",
        "History",
        "Shopping"
    ]
)

# ---------------- GENERATE TRIP ---------------- #

if st.button("Generate My Goa Trip"):

    with st.spinner("Creating your personalized Goa itinerary..."):

        itinerary = generate_itinerary(
            people,
            days,
            budget,
            kids_0_5,
            kids_6_10,
            elders,
            food_pref,
            interests
        )

    st.success("Your travel plan is ready!")

    st.subheader("📍 Your Personalized Goa Itinerary")
    st.markdown(itinerary)

    # Extract places dynamically from itinerary
    places = extract_places(itinerary)

    if places:
        st.subheader("🗺 Locations Mentioned in Your Itinerary")

        for place in places[:5]:
            link = get_map_link(place)
            st.markdown(f"📍 [{place}]({link})")

# ---------------- FOOTER ---------------- #

st.markdown("---")
st.caption("GoaGenie AI Travel Planner • Powered by Local AI (Phi-3)")