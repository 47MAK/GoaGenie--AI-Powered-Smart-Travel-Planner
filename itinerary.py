import json
from openai import OpenAI

client = OpenAI(
    api_key="3wRPmTCH5hlcooOBHLgp4u1YpYsa55JcCuDRRwRhdbnVPINtiAdJ8bEibNCKpDS4B",
    base_url="https://api.stepfun.com/v1"
)


def generate_itinerary(people, days, budget, kids, elders, food_pref, interests):

    with open("goa_places.json", "r") as f:
        places = json.load(f)

    prompt = f"""
You are an expert travel planner.

Create a {days}-day travel itinerary for Goa.

Travelers: {people}
Budget: {budget}
Kids travelling: {kids}
Elders travelling: {elders}
Food preference: {food_pref}
Interests: {interests}

Available places:
{places}

Generate a structured itinerary:

Day 1
Morning:
Afternoon:
Lunch:
Evening:

Also suggest famous Goan food.
"""

    try:
        response = client.chat.completions.create(
            model="step-1-8k",
            messages=[
                {"role": "system", "content": "You are a helpful travel planning assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error generating itinerary: {str(e)}"