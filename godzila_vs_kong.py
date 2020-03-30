budget = float(input("Film's budget :"))
statists = int(input("Number of statists: "))
clothing_statist = float(input("Enter clothing price for one statist: "))

environment = 0.1 * budget

# budget = budget - environment

if statists > 150:
    clothing_statist = clothing_statist - (0.1 * clothing_statist)

total_money = statists * clothing_statist + environment

if budget < total_money:
    print('Not enough money!')
    print(f"Wingard needs {total_money - budget:.2f}")
elif budget >= total_money:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_money:.2f} leva left.")
