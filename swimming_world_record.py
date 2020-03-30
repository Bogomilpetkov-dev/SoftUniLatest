from math import floor

record = float(input("Enter time to beat:"))
length = float(input("Length:"))
one_meter = float(input("Enter Ivan's time for 1 meter:"))

multiplier = floor(length // 15)

time = length * one_meter + multiplier * 12.5

if time > record:
    print(f"No , he failed! he was {time-record:.2f} seconds slower.")

elif time < record:

    print(f"Yes , he succeeded! The new world record is {time:.2f} seconds.")