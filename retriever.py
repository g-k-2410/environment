def get_recommendations(transport, diet, electricity, shopping_freq):
    tips = []

    if transport in ["Car", "Electric Vehicle"]:
        if transport == "Car":
            tips.append("Reducing car use, even occasionally, can lower emissions significantly.")
        else:
            tips.append("Using an electric vehicle is great—try charging during off-peak hours or using solar.")

    elif transport in ["Public Transport", "Cycle/Walk"]:
        tips.append("Efficient transport choice! You're helping reduce traffic and pollution.")

    if diet in ["Meat-heavy", "Mixed"]:
        if diet == "Meat-heavy":
            tips.append("Try reducing meat intake gradually—start with one meatless day per week.")
        else:
            tips.append("A mostly plant-based diet is great—keep balancing your meals.")

    elif diet in ["Vegetarian", "Vegan"]:
        tips.append("Excellent! Your food choices support lower emissions and water use.")

    if electricity > 600:
        tips.append("High usage detected—consider a home energy audit or smart meters.")
    elif 300 < electricity <= 600:
        tips.append("Moderate electricity usage—optimize with efficient appliances and habits.")
    else:
        tips.append("Nice! Low electricity use means a smaller carbon footprint.")

    if shopping_freq == "Every week":
        tips.append("Weekly shopping can add up. Try buying only what you need or explore second-hand options.")
    elif shopping_freq == "Monthly":
        tips.append("Monthly shopping is better. Sustainable brands or thrift stores can further reduce impact.")
    else:
        tips.append("Minimal shopping habits are great for both the planet and your wallet!")

    return tips
