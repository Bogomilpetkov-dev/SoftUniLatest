trans = int(input("Transactions:"))
bank_balance = 0
count = 0
while count < trans:
    curr_money = float(input("Money to be inserted:"))

    print(f"Increase {curr_money}")
    if curr_money < 0:
        print("Invalid operation!")
        break
    bank_balance = bank_balance + curr_money
    count=count+1
print(f"Total: {bank_balance:.2f}")
