width=int(input("Width:"))
length=int(input("Length:"))

total_pieces=width*length
total_cut=0
while total_pieces >= total_cut:
    cut=input("Enter amount:")
    if cut=="STOP" and total_cut < total_pieces:

        print(f"{abs(total_cut - total_pieces)} pieces are left.")

        break

    else:
        cut=int(cut)
    total_cut=total_cut + cut
if total_pieces < total_cut :
    print(f"No more cake left! You need {abs(total_pieces-total_cut)} pieces more.")
# print(total_cut)