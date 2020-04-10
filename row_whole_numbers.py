import sys
count=int(input("Numbers count:"))

max_num=-sys.maxsize
min_num=sys.maxsize

for counter in range(count):
    number=int(input("Enter number:"))
    if number > max_num:
        max_num=number
    if number <min_num:
        min_num=number

print(f"Max number: {max_num}")
print(f"Min number: {min_num}")