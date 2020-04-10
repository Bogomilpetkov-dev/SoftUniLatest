from math import floor
year = input("Type of year:")
holidays = int(input("Holidays in one year:"))
travel_weekend = int(input("Weekends that Vlady travels to his city:"))

volley_weekends = (48 - travel_weekend)*3/4  # 3/4*48  ; 12 weekends he work

if travel_weekend:
    sofia_volley = volley_weekends   # we have only saturday for play
    travel_volley = travel_weekend

if holidays:
    volley_holidays=2/3 * holidays

total_days_to_play = volley_holidays + sofia_volley + travel_volley

if year == "leap":
    total_days_to_play = int((total_days_to_play * 1.15)//1)

    print(total_days_to_play)
elif year == "normal":
    total_days_to_play=int( total_days_to_play//1)

    print(total_days_to_play)


