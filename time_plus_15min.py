hour = int(input("Enter hour:"))
minutes = int(input("Enter minutes:"))

if 0 <= minutes <= 44 and 0 <= hour <= 23:
    minutes = minutes + 15
    if hour == 24:
        hour=0
    print(f"{hour}:{minutes}")
elif 44 < minutes < 55 and 0 <= hour <= 23:
    hour = hour + 1
    extra = (minutes + 15) - 60
    if hour==24:
        hour=0
    print(f"{hour}:{extra:02d}")
elif 55 <= minutes <= 59 and 0 <= hour <= 23:
    extra = (minutes + 15) - 60
    hour = hour + 1
    if hour==24:
        hour=0
    print(f'{hour}:{extra:02d}')



