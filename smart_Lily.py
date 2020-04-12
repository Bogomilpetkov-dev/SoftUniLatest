age = int(input("Age:"))
washing_m = float(input("washing machine's price:"))
toy_price = int(input("Toy price:"))

toy_money = 0
cash = 10
sum_cash = 0

for count in range(1, age +1):
    if count % 2 == 1:
        toy_money = toy_money + toy_price
    elif count % 2 == 0 and count > 0:
        sum_cash = sum_cash + cash
        cash=cash+10


total = sum_cash + toy_money - (age//2)

if total >= washing_m :
    print(f"Yes! {total-washing_m:.2f} left!")
else:
    print(f"No! {abs(toy_money-total):.2f} more needed.")