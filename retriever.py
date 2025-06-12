def estimate_footprint(transport, diet, electricity, shopping_freq):
    score = 0.0

    # Transport score (fuzzy weights)
    transport_weights = {
        "Car": 1.0,
        "Electric Vehicle": 0.4,
        "Public Transport": 0.5,
        "Cycle/Walk": 0.1
    }
    score += 30 * transport_weights.get(transport, 0.6)

    # Diet score (fuzzy weights)
    diet_weights = {
        "Meat-heavy": 1.0,
        "Mixed": 0.67,
        "Vegetarian": 0.33,
        "Vegan": 0.1
    }
    score += 30 * diet_weights.get(diet, 0.5)

    # Electricity score (linear fuzzy logic)
    if electricity > 600:
        score += 20
    elif electricity > 300:
        score += 10 + (10 * ((electricity - 300) / 300))  # smooth transition
    else:
        score += 5 + (5 * (electricity / 300))  # low usage still has gradation

    # Shopping score (fuzzy mapping)
    shopping_weights = {
        "Every week": 1.0,
        "Monthly": 0.66,
        "Rarely": 0.33
    }
    score += 15 * shopping_weights.get(shopping_freq, 0.2)

    return round(score, 2)
