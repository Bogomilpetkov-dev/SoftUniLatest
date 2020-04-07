celcius = int(input("Enter celcius:"))
time_of_the_day=input("Enter time of the day:")

if 10<= celcius <=18:
    if time_of_the_day=="Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif time_of_the_day=="Afternoon":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time_of_the_day=="Evening":
        outfit="Shirt"
        shoes="Moccasins"
elif 18< celcius <=24:
    if time_of_the_day=="Morning":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time_of_the_day=="Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time_of_the_day=="Evening":
        outfit="Shirt"
        shoes="Moccasins"
elif celcius >=25:
    if time_of_the_day=="Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time_of_the_day=="Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif time_of_the_day=="Evening":
        outfit="Shirt"
        shoes="Moccasins"

print(f"It's {celcius}degrees , get your {outfit} and {shoes}.")