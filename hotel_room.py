month=input("Enter month:")
overnight=float(input("Overnights:"))

if month=="May" or month=="October":
    studio=50
    apartment=65
    if overnight > 14:
        studio=0.70*studio
    elif overnight > 7:
        studio=0.95*studio

elif month=="June" or month=="September":
    studio=75.20
    apartment=68.70
    if overnight > 14:
        studio=0.80*studio

elif month=="July" or month=="August":
    studio=76
    apartment=77

if overnight > 14:
    apartment=0.90*apartment

print(f"Apartment: {overnight*apartment:.2f} lv.")
print(f"Studio: {overnight*studio:.2f} lv.")