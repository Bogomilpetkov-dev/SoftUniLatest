type = input("Type of flower:")
amount = int(input("Amount of flowers:"))
budget = int(input("Budget:"))

price=0
final=0

if type == "Roses":
    price = 5
    if amount > 80:
        final = amount * price * 0.9
    else:
        final = amount *price
elif type == "Dahlias":
    price = 3.8
    if amount > 90:
        final = amount * price * 0.85
    else:
        final = amount * price
elif type == "Tulips":
    price = 2.8
    if amount > 80 :
        final = amount * price * 0.85
    else:
        final = amount * price
elif type == "Narcissus":
    price = 3
    if amount > 120 :
        final = amount * price
    else:
        final = amount * price * 1.15
elif type == "Gladiolus":
    price = 5
    if amount > 80 :
        final = amount * price
    else:
        final = amount * price * 1.20

if budget >= final:
    print(f"Hey, you have a great garden with {amount} {type} and"
          f" {budget - final:.2f} leva left.")
else:
    print(f"Not enough money, you need {final - budget:.2f} leva more.")