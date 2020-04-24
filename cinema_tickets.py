total=0
counter=0
kid=0
student=0
standard=0
while True:
    film_name = input("Film:")
    if film_name == "Finish":
        break
    free_seats = int(input("Seats:"))
    while True:
        if free_seats >= counter:
            type_ticket = input("Ticket type:")
            if type_ticket=="standard":
                standard=standard+1
                counter = counter + 1
                total=total+1

            elif type_ticket=="kid":
                kid=kid+1
                counter = counter + 1
                total=total+1

            elif type_ticket=="student":
                student=student+1
                counter=counter+1
                total=total+1

            elif type_ticket=="End":
                print(f"{film_name} - {((counter / free_seats)*100):.2f}% full.")
                counter=0
                break
        elif counter >= free_seats:
            break
print(f"Total tickets: {total}")

print(f"{((student/total)*100):.2f}% student tickets.")
print(f"{((standard/total)*100):.2f}% standard tickets.")
print(f"{((kid/total)*100):.2f}% kids tickets.")




