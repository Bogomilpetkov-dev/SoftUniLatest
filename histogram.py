n = int(input("amount:"))

p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0
for count in range(0, n):
    num = int(input("Enter num:"))
    if 0 < num < 200:
        p1_count=p1_count+1
    elif 200 <= num < 400:
        p2_count=p2_count+1
    elif 400 <= num < 600:
        p3_count=p3_count+1
    elif 600 <= num < 800:
        p4_count=p4_count+1
    elif num >= 800:
        p5_count=p5_count+1

print(f"{(p1_count/n * 100):.2f}%")
print(f"{(p2_count/n * 100):.2f}%")
print(f"{(p3_count/n * 100):.2f}%")
print(f"{(p4_count/n * 100):.2f}%")
print(f"{(p5_count/n * 100):.2f}%")