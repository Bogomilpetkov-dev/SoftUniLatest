N1=int(input("Enter first number:"))
N2=int(input("Enter second number:"))
operator=input("Enter operator:")

if operator == "+":
    result = (N1 + N2)
    if result % 2 == 0:
        even_or_odd="even"
        print(f"{N1}{operator}{N2} = {N1+N2} - {even_or_odd}")
    elif result % 2 == 1:
        even_or_odd="odd"
        print(f"{N1}{operator}{N2} = {N1+N2} - {even_or_odd}")
elif operator == "-":
    result = (N1 - N2)
    if result % 2 == 0:
        even_or_odd = "even"
        print(f"{N1}{operator}{N2} = {N1 - N2} - {even_or_odd}")
    elif result % 2 == 1:
        even_or_odd = "odd"
        print(f"{N1}{operator}{N2} = {N1 - N2} - {even_or_odd}")
elif operator == "*":
    result = (N1 * N2)
    if result % 2 == 0:
        even_or_odd = "even"
        print(f"{N1}{operator}{N2} = {N1 * N2} - {even_or_odd}")
    elif result % 2 == 1:
        even_or_odd = "odd"
        print(f"{N1}{operator}{N2} = {N1 * N2} - {even_or_odd}")
elif N2==0:
    print(f"Cannot divide {N1} by zero")
elif operator=="/":
    print(f"{N1} {operator} {N2} = {N1/N2:.2f}")
elif operator=="%":
    print(f"{N1} {operator} {N2} = {N1%N2}")

