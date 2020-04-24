first = int(input())
second = int(input())
magic = int(input())
counter = 0
is_found=False
for num in range(first, second + 1):
    for number in range(first, second + 1):
        counter += 1
        if num + number == magic:

            is_found=True
            print(f"Combination N:{counter}  ({num} + {number} = {magic})")
        if is_found== True:
            break
if is_found == False:

    print(f"{counter} combinations - neither equals {magic}")
