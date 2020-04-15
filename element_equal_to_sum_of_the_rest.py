import sys

count = int(input("Enter amount:"))
max_size = -sys.maxsize
sum_num = 0
other = 0

for x in range(0, count):
    num = int(input("Enter num:"))
    if max_size > num:
        other = num
    else:
        max_size = num
    sum_num = sum_num + num

print(max_size)
print(sum_num)

other_sum=sum_num - max_size

if (other_sum) == max_size:
    print("Yes")
    print(f"Sum = {max_size}")
else:
    print("No")
    print(f"Diff = {abs(max_size - other_sum)}")