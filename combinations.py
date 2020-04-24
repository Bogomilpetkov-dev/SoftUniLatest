n=int(input())
counter=0
for x1 in range(n+1):
    for x2 in range(n+1):
        for x3 in range(n+1):

            result=x1+x2+x3
            if result == n:
                counter=counter+1
                # print(f"{x1} + {x2} + {x3} = {result}")
print(counter)




# result=x1+x2+x3
#             if result == n:
#                 print(f"{x1} + {x2} + {x3} = {result}")