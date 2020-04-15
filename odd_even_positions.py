import sys

n = int(input("Amount:"))

even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize

odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
for x in range(1, n + 1):
    print(x)
    num = float(input("Number:"))
    if x % 2 == 0:
        even_sum = even_sum + num
        if num < even_min:
            even_min = num
        elif num > even_max:
            even_max = num
    else:
        odd_sum = odd_sum + num
        if num > odd_max:
            odd_max = num
        elif num < odd_min:
            odd_min = num

if n == 1:
    even_min = "No"
    even_max = "No"
    odd_min = odd_max
if n == 0:
    odd_min = "No"
    odd_max = "No"
    even_min = "No"
    even_max = "No"

print(f"OddSum={odd_sum:.2f},")
print(f"OddMin={odd_min:.2f},")
print(f"OddMax={odd_max:.2f},")
print(f"EvenSum={even_sum:.2f},")
print(f"EvenMin={even_min:.2f},")
print(f"EvenMax={even_max:.2f}")


