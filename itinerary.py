import json
import ollama


def generate_itinerary(people, days, budget, kids, elders, food_pref, interests):

    try:
        # Load Goa places dataset
        with open("goa_places.json", "r") as f:
            places = json.load(f)

        # Reduce dataset size sent to model
        beaches = places.get("beaches", [])
        attractions = places.get("attractions", [])
        restaurants = places.get("restaurants", [])
        foods = places.get("foods", [])

        prompt = f"""
You are an expert travel planner.

Create a concise {days}-day itinerary for Goa.

Trip details:
Travelers: {people}
Budget: {budget}
Kids: {kids}
Elders: {elders}
Food preference: {food_pref}
Interests: {interests}

Suggested beaches: {beaches}
Suggested attractions: {attractions}
Suggested restaurants: {restaurants}

Format:

Day 1
Morning:
Afternoon:
Lunch:
Evening:

Day 2
Morning:
Afternoon:
Lunch:
Evening:

Also recommend one famous Goan dish per day from:
{foods}

Limit the response to about 150 words.
"""

        # Faster Ollama generation
        response = ollama.chat(
            model="phi3",
            messages=[{"role": "user", "content": prompt}],
            options={
                "num_predict": 200,   # limit output tokens (faster)
                "temperature": 0.7
            }
        )

        itinerary = response["message"]["content"]

        return itinerary

    except Exception as e:
        return f"Error generating itinerary: {str(e)}"