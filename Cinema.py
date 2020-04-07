type = input("Enter type of projection:")
rows = int(input("Rows:"))
columns = int(input("Columns:"))
price = 0

if type == "Premiere":
    ticket = 12
elif type == "Normal":
    ticket = 7.5
elif type == "Discount":
    ticket = 5

price = ticket * rows * columns

print(f"{price:.2f} leva")
