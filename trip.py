
while True:
    destination = input()
    if destination=="End":
        break
    min_budget = int(input())
    while True:
        saved=int(input())

        min_budget=min_budget-saved
        if min_budget <= 0:
            print(f"Going to {destination}!")

            break
