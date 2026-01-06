def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    name = seed_type.capitalize()

    if unit == "packets":
        print(f"{name}: {quantity} {unit} available")
    elif unit == "grams":
        print(f"{name}: {quantity} {unit} total")
    elif unit == "area":
        print(f"{name}: covers {quantity} square meters")
    else:
        print("Unknown unit type")
