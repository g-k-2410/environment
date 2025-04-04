def get_recommendations(transport, diet, electricity, shopping_freq):
    tips = []

    if transport == "Car":
        tips.append("Consider carpooling or switching to public transport to reduce emissions.")
    elif transport == "Electric Vehicle":
        tips.append("Great job! Charging with renewable energy can further reduce your footprint.")

    if diet == "Meat-heavy":
        tips.append("Try reducing red meat intake. Even one meat-free day per week helps.")
    elif diet == "Vegan":
        tips.append("Awesome! Plant-based diets are among the most sustainable.")

    if electricity > 500:
        tips.append("Switch to energy-efficient appliances and LED lighting.")
    else:
        tips.append("Your electricity usage is relatively low. Keep it up!")

    if shopping_freq in ["Every week", "Monthly"]:
        tips.append("Try second-hand or upcycled clothing to reduce fast fashion waste.")
    else:
        tips.append("Minimal shopping habits reduce environmental impact.")

    return tips
