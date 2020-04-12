count = int(input("count:"))
counter=count
sum_left = 0
sum_right = 0

for counter in range(0, count):
    left = int(input("left:"))
    sum_left = sum_left + left

print(count)

for counter in range(0, count):
    right = int(input("right:"))
    sum_right = sum_right + right

print(sum_left)
print(sum_right)

if sum_left == sum_right:
    print(f"Yes, sum = {sum_left}")
else:
    print(f"No, diff is = {abs(sum_left-sum_right)}")