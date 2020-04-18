import sys
n = int(input("Enter count:"))
count = 0
smallest_num = sys.maxsize
while count < n:
    num = int(input("Enter num:"))
    if num < smallest_num:
        smallest_num = num


    count = count + 1
print(smallest_num)