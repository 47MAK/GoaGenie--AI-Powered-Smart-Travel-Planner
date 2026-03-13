import re


def extract_places(itinerary):

    # Find capitalized word sequences (possible places)
    pattern = r'\b[A-Z][a-zA-Z]+(?:\s[A-Z][a-zA-Z]+)*\b'

    matches = re.findall(pattern, itinerary)

    ignore_words = {
        "Day", "Morning", "Afternoon", "Lunch", "Evening",
        "Visit", "Enjoy", "Start", "Head", "Have", "Goa",
        "Kids", "Elders", "Budget", "Travelers"
    }

    places = []

    for match in matches:

        # ignore single words that are likely verbs
        if match in ignore_words:
            continue

        # prefer 2–4 word phrases
        word_count = len(match.split())

        if word_count >= 2 and word_count <= 4:

            if match not in places:
                places.append(match)

        # stop when we have enough
        if len(places) == 5:
            break

    return places


def get_map_link(place):

    query = place.replace(" ", "+")
    return f"https://www.google.com/maps/search/{query}"