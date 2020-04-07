budget = float(input("Budget:"))
season = input("Season:")

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        spendings = budget * 0.30
        place="Camp"
    elif season == "winter":
        place = "Hotel"
        spendings = budget * 0.70
elif budget <= 1000:
    destination="Balkans"
    if season == "summer":
        place = "Camp"
        spendings = budget * 0.40
    elif season == "winter":
        place = "Hotel"
        spendings = budget * 0.80
elif budget > 1000 and season == "summer" or season == "winter":
    place="Hotel"
    spendings = budget * 0.90
    destination = "Europe"

print(f"Somewhere in {destination} , {place} , { spendings:.2f}")