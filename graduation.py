name=input("Name:")
count=1
sum_grade=0
while count < 13:
    grade=float(input("Enter grade:"))
    if grade >= 4:
        sum_grade=sum_grade+grade
    else:
        count=count-1
    count=count+1

print(f"{name} graduated. Average grade: {(sum_grade/12):.2f}")
