def estimate_footprint(transport, diet, electricity, shopping_freq):
    score = 0

    # Transport score
    if transport == "Car":
        score += 30
    elif transport == "Public Transport":
        score += 15
    elif transport == "Cycle/Walk":
        score += 5
    elif transport == "Electric Vehicle":
        score += 10

    # Diet score
    if diet == "Meat-heavy":
        score += 30
    elif diet == "Mixed":
        score += 20
    elif diet == "Vegetarian":
        score += 10
    elif diet == "Vegan":
        score += 5

    # Electricity score
    if electricity > 600:
        score += 20
    elif electricity > 300:
        score += 10
    else:
        score += 5

    # Shopping score
    if shopping_freq == "Every week":
        score += 15
    elif shopping_freq == "Monthly":
        score += 10
    elif shopping_freq == "Rarely":
        score += 5
    else:
        score += 2

    return score
