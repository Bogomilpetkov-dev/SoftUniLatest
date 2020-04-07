
x1 = float(input("X1="))
y1 = float(input("Y1="))
x2 = float(input("X2="))
y2 = float(input("Y2="))
x = float(input("X="))
y = float(input("Y="))

first_condition = (x == x1 or x == x2) and (y1 <= y <=y2)
second_condition = (y == y1 or y == y2) and (x1 <= x <= x2)

if first_condition or second_condition:
    print("Border")
else:
    print("Inside / Outside")

