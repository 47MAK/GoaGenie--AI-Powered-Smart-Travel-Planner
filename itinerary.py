import json
import random

# Load Goa dataset
with open("goa_places.json", "r") as f:
    data = json.load(f)

beaches = data["beaches"]
attractions = data["attractions"]
restaurants = data["restaurants"]
foods = data["foods"]


def generate_itinerary(people, days, budget, kids, elders, food_pref, interests):

    itinerary = ""

    itinerary += f"Trip Plan for {people} people for {days} days\n"
    itinerary += f"Budget: {budget}\n\n"

    for day in range(1, days + 1):

        itinerary += f"Day {day}\n"

        if "Beaches" in interests:
            itinerary += f"Morning: Visit {random.choice(beaches)}\n"
        else:
            itinerary += f"Morning: Explore {random.choice(attractions)}\n"

        itinerary += f"Afternoon: Visit {random.choice(attractions)}\n"

        itinerary += f"Lunch: Eat at {random.choice(restaurants)}\n"

        itinerary += f"Evening: Relax at {random.choice(beaches)}\n"

        itinerary += "\n"

    itinerary += "Must Try Goan Foods:\n"

    for food in foods:
        itinerary += f"- {food}\n"

    return itinerary