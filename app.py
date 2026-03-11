import streamlit as st
from itinerary import generate_itinerary

# App title
st.set_page_config(page_title="GoaGenie", page_icon="🌴")

st.title("🌴 GoaGenie")
st.subheader("AI Travel Planner for Goa")

st.write("Plan your perfect Goa trip based on your preferences.")

# -------- USER INPUTS --------
st.header("Enter Trip Details")

people = st.number_input("Number of People", min_value=1, max_value=20, value=2)

days = st.slider("Trip Duration (Days)", 1, 10, 3)

budget = st.selectbox(
    "Budget",
    ["Low", "Medium", "Luxury"]
)

kids = st.selectbox(
    "Traveling with Kids?",
    ["Yes", "No"]
)

elders = st.selectbox(
    "Traveling with Elders?",
    ["Yes", "No"]
)

food_pref = st.selectbox(
    "Food Preference",
    ["Vegetarian", "Non-Vegetarian", "Both"]
)

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

# -------- GENERATE BUTTON --------
if st.button("Generate My Goa Trip"):

    with st.spinner("Creating your personalized Goa itinerary..."):
        
        itinerary = generate_itinerary(
            people,
            days,
            budget,
            kids,
            elders,
            food_pref,
            interests
        )

    st.success("Your travel plan is ready!")

    st.subheader("📍 Your Personalized Goa Itinerary")

    st.write(itinerary)

st.markdown("---")
st.caption("GoaGenie AI Travel Planner • Built with Streamlit")