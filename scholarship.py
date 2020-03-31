from math import floor

income = float(input("Family income: "))
average_succes = float(input("Enter average succes: "))
min_salary = float(input("Enter minimal working salary: "))

bonus = 0
if income > min_salary:
    if average_succes < 5.5:
        print("You cannot get a scholarship!")
elif average_succes >= 5.5:
    if min_salary > income:
        other_posibility = (min_salary * 0.35)
        bonus = floor(average_succes * 25)
        if bonus < other_posibility:
            other_posibility = floor(other_posibility)
            print(
                f"You can get both social and for excellent results , but you get the "
                f"higher one: {other_posibility} BGN")
        elif bonus > other_posibility:
            bonus=floor(bonus)
            print(f"You can get both social and for excellent results , but you "
                  f"get the higher one: {bonus} BGN")
elif average_succes >= 5.5:
    bonus = floor(average_succes * 25)
    print(f"You get scholarship for excellent results {bonus} BGN")

elif average_succes >= 4.5:
    if min_salary > income:
        bonus = floor(0.35 * min_salary)
        print(f"You get a Social scholarship {bonus} BGN")
