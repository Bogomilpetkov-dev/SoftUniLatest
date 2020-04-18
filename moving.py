width = int(input("Width:"))
length = int(input("Length:"))
height = int(input("Height:"))

free = width * length * height
sum_current = 0



# if current == "Done":
#     print(f"{abs(free - sum_current)} Cubic meters left.")

while free > 0:
    command = input("Enter volume:")
    if command == "Done":
        print(f"{abs(free - sum_current)} Cubic meters left.")
        break
    else:
        command = int(command)
        sum_current=sum_current+command

    if free-sum_current == 0 or sum_current>free:
        print(f"No more free space! You need {abs(sum_current - free)} Cubic meters more.")
        break

