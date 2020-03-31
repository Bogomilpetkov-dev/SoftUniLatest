time_first = int(input("Enter first time:"))
time_second = int(input("Enter second time:"))
time_third = int(input("Enter third time:"))

time_total = time_first + time_second + time_third

minutes = time_total // 60
seconds = time_total % 60

if seconds <= 9:
    #seconds = f'{seconds:01}'
    print(f"The summary time of the three times is : {minutes}:0{seconds}")
else:
    print(f"The summary time of the three times is : {minutes}:{seconds}")

