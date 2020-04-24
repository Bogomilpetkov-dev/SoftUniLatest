floors = int(input())
rooms = int(input())

for i in range(floors, 0, -1):
    for b in range(0, rooms):

        if i==floors or floors==1 :

           print(f"L{i}{b}", end=" ")
        elif i != floors :
            if i % 2 ==0:
                print(f"O{i}{b}", end=" ")
            elif  i % 2 ==1:
                print(f"A{i}{b}", end=" ")

    print()




