n = int(input("Amount"))

p1_count = 0
p2_count = 0
p3_count = 0

for count in range(0, n):
    num = int(input("Number:"))
    if num % 2 == 0:
        p1_count = p1_count + 1
    if num % 3 == 0:
        p2_count = p2_count + 1
    if num % 4 == 0:
        p3_count = p3_count + 1

print(f"{(p1_count/n*100):.2f}%")
print(f"{(p2_count/n*100):.2f}%")
print(f"{(p3_count/n*100):.2f}%")
