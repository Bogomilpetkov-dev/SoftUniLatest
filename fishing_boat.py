budget = int(input("Enter budget:"))
season = input("Season:")
fishermen = int(input("Fishermen:"))

if season == "Spring":
    price=3000
elif season == "Summer":
    price=4200
elif season == "Autumn":
    price=4200
elif season == "Winter":
    price=2600

if fishermen <=6:
    price=price*0.9
elif 6 < fishermen <= 11:
    price=price*0.85
elif fishermen > 12:
    price=price*0.75

if fishermen % 2 == 0:
    if season=="Spring" or season=="Summer" or season=="Winter":
        price=price*0.95

if budget >= price:
    print(f"Yes! You have {budget-price:.2f}leva left.")
else:
    print(f"Not enough money! You need {price-budget:.2f}leva.")