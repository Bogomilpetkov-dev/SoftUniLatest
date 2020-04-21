wanted_book=input("Enter wanted book:")
capacity=int(input("Amount:"))
book=""
amount=0
while wanted_book != book:
    book=input("Enter book that you have:")
    amount=amount+1
    if capacity == amount:
        print("The book you searched is not here!")
        print(f"You checked {amount} books.")
        break
if wanted_book == book:
    amount=amount -1
    print(f"You checked {amount} books and found it.")


