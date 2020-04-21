unsatisfied_marks = int(input("Unsatisfied marks:"))
marks_below = 0
marks_total = 0
num=0
last=''
while unsatisfied_marks >= marks_below:

    name = input("Enter name:")
    if name == "Enough":
        print(f"Average score: {(marks_total/num):.2f}")
        print(f"Number of problems: {num}")
        print(f"Last problem: {last}")
        break
    curr_mark = int(input("Enter mark:"))

    if curr_mark <= 4:
        marks_below = marks_below + 1
        if unsatisfied_marks <= marks_below:
            print(f"You need a break, {unsatisfied_marks} poor grades.")
            break
    elif curr_mark > 4:

        last=name
    marks_total = marks_total + curr_mark
    num = num + 1



