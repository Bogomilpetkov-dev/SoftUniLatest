name = input("Name:")
count = 0
sum_grade = 0

fail = 0

while count < 12:
    grade = float(input("Grade:"))
    if grade >= 4:
        sum_grade = sum_grade + grade
    elif grade < 4:
        fail = fail + 1
        if fail > 1:
            print(f"{name} has been excluded at {count} grade")
            break
    count=count+1
    if count==12:
        average=sum_grade/12
        print(f"{name} graduated. Average grade: {average:.2f}")
