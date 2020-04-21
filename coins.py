rest = float(input("Enter amount:"))
rest_converted = int(rest * 100)
sum_coins = 0

double_lev = 0
lev_coef = 0
fifty_coef = 0
twenty_coef = 0
ten_coef = 0
five_coef = 0
two_coef = 0
one_coef = 0

while not rest_converted <= sum_coins:
    if rest_converted // 200 != 0 and rest_converted >= 200:
        double_lev = double_lev + (rest_converted // 200)
        rest_converted = rest_converted - (double_lev * 200)

    if rest_converted // 100 == 1:
        lev_coef = lev_coef + (rest_converted // 100)
        rest_converted = rest_converted - (lev_coef * 100)

    if rest_converted // 50 != 0 and rest_converted >= 50:
        fifty_coef = fifty_coef + (rest_converted // 50)
        rest_converted = rest_converted - (fifty_coef * 50)

    if rest_converted // 20 != 0 and rest_converted >= 20:
        twenty_coef = twenty_coef + (rest_converted // 20)
        rest_converted = rest_converted - (twenty_coef * 20)

    if rest_converted // 10 != 0 and rest_converted >= 10:
        ten_coef = ten_coef + (rest_converted // 10)
        rest_converted = rest_converted - (ten_coef * 10)

    if rest_converted // 5 != 0 and rest_converted >= 5:
        five_coef = five_coef + (rest_converted // 5)
        rest_converted = rest_converted - (five_coef * 5)

    if rest_converted // 2 != 0 and rest_converted >= 2:
        two_coef = two_coef + (rest_converted // 2)
        rest_converted = rest_converted - (two_coef * 2)

    if rest_converted // 1 != 0 and rest_converted >= 1:
        one_coef = one_coef + (rest_converted // 1)
        rest_converted = rest_converted - one_coef

    sum_coins = double_lev + lev_coef + fifty_coef + twenty_coef +ten_coef + five_coef + two_coef + one_coef
    break
print(sum_coins)


