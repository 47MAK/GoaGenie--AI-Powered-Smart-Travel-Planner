import random

# Sample Goa places dataset

beaches = ["Baga Beach", "Calangute Beach", "Anjuna Beach", "Vagator Beach", "Colva Beach"]
attractions = ["Fort Aguada", "Chapora Fort", "Basilica of Bom Jesus", "Dudhsagar Waterfalls"]
restaurants_veg = ["Navtara Veg Restaurant", "Bean Me Up", "Blue Planet Cafe"]
restaurants_nonveg = ["Fisherman's Wharf", "Britto's", "Martin's Corner"]
nightlife = ["Tito's Lane", "Mambo's Club", "Curlies Beach Shack"]


def generate_itinerary(people, days, budget, kids, elders, food_pref, interests):

    itinerary = ""

    itinerary += f"Trip Plan for {people} people for {days} days\n"
    itinerary += f"Budget: {budget}\n\n"

    for day in range(1, days + 1):

        itinerary += f"Day {day}\n"

        # Morning activity
        if "Beaches" in interests:
            itinerary += f"Morning: Visit {random.choice(beaches)}\n"
        else:
            itinerary += f"Morning: Explore {random.choice(attractions)}\n"

        # Afternoon activity
        itinerary += f"Afternoon: Visit {random.choice(attractions)}\n"

        # Lunch
        if food_pref == "Vegetarian":
            itinerary += f"Lunch: Eat at {random.choice(restaurants_veg)}\n"
        elif food_pref == "Non-Vegetarian":
            itinerary += f"Lunch: Eat at {random.choice(restaurants_nonveg)}\n"
        else:
            itinerary += f"Lunch: Eat at {random.choice(restaurants_veg + restaurants_nonveg)}\n"

        # Evening activity
        if "Nightlife" in interests:
            itinerary += f"Evening: Enjoy nightlife at {random.choice(nightlife)}\n"
        else:
            itinerary += f"Evening: Sunset at {random.choice(beaches)}\n"

        itinerary += "\n"

    itinerary += "Must Try Goan Foods:\n"
    itinerary += "- Goan Fish Curry\n"
    itinerary += "- Bebinca\n"
    itinerary += "- Prawn Balchao\n"
    itinerary += "- Cashew Feni\n"

    return itinerary