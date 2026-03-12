import json
import ollama

def generate_itinerary(people, days, budget, kids, elders, food_pref, interests):

    with open("goa_places.json", "r") as f:
        places = json.load(f)

    prompt = f"""
Create a {days}-day travel itinerary for Goa.

Travelers: {people}
Budget: {budget}
Kids travelling: {kids}
Elders travelling: {elders}
Food preference: {food_pref}
Interests: {interests}

Available places:
{places}

Generate a structured itinerary with morning, afternoon, lunch, and evening activities.
"""

    response = ollama.chat(
       model="phi3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]