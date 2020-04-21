few = 0
sum_steps = 0
while sum_steps < 10000:
    steps = input("Steps made:")
    if steps == "Going home":
        few = int(input("Steps made to home:"))
        break
    steps = int(steps)
    sum_steps = steps + sum_steps + few

sum_steps = sum_steps + few

if sum_steps < 10000:
    left=10000-sum_steps
    print(f"{left} more steps to reach goal.")
else:
    print("Goal reached! Good job!")





