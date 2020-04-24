floor = int(input())
rooms = int(input())
for floor_number in range(floor, 0, -1):

    for room_number in range(0, rooms):
        if floor_number == floor:
            print(f"L{floor_number}{room_number}", end=" ")
        elif floor_number % 2 == 1:
            print(f"A{floor_number}{room_number}", end=" ")
        elif floor_number % 2 == 0:
            print(f"O{floor_number}{room_number}", end=" ")
    print()