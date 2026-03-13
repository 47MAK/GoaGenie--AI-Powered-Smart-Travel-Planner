import ollama


def generate_itinerary(people, days, budget, kids_0_5, kids_6_10, elders, food_pref, interests):

    if "Low" in budget:
        budget_range = "₹1000–₹2500 per person per day"
    elif "Medium" in budget:
        budget_range = "₹2500–₹6000 per person per day"
    else:
        budget_range = "₹6000–₹15000+ per person per day"

    prompt = f"""
You are an expert Goa travel planner.

Generate a COMPLETE {days}-day itinerary for Goa.


Travelers: {people}
Budget range: {budget_range}
Food preference: {food_pref}

Kids age 0-5: {kids_0_5}
Kids age 6-10: {kids_6_10}
Elders age 60+: {elders}

Interests: {interests}

Rules:
- You MUST generate exactly {days} days.
- Do NOT stop early.
- Respect vegetarian preference if selected.
- Suggest kid-friendly places if children present.
- Avoid physically demanding activities if elders present.
- Activities must match the selected interests.
- Keep recommendations within the specified budget range.

Format:

Day 1
Morning:
Afternoon:
Lunch:
Evening:

Mention if the activity is good for kids or elders.
Limit response to about 200-250 words.
"""

    response = ollama.chat(
        model="phi3",
        messages=[{"role": "user", "content": prompt}],
        options={
            "num_predict": 800,
            "temperature": 0.7
        }
    )

    return response["message"]["content"]