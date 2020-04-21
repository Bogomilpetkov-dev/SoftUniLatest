money_needed = float(input("Money needed:"))
money_atm = float(input("Money at the moment:"))
times_spendings = 0
days_passed = 0
money_saved_total = 0
money_final = 0

while not money_final >= money_needed:
    action = input("Action:")
    money_save_or_spend = float(input("Money saved for the day:"))
    days_passed = days_passed + 1
    if action == "save":
        money_saved_total = money_saved_total + money_save_or_spend
        money_final = money_atm + money_saved_total
        times_spendings=0
    elif action == "spend":
        times_spendings = times_spendings + 1
        if money_save_or_spend >= money_atm:
            money_save_or_spend = money_atm
        else:
            money_atm = money_atm - money_save_or_spend

    if times_spendings == 5:
        print(f"You can't save the money.")
        print(days_passed)
        break
    elif money_final >= money_needed:
        print(f"You saved the money for {days_passed} days.")



