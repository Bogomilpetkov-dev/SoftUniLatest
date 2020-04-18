command = input()
sum_num = 0
while command != 'stop':
    current_com = int(command)
    sum_num = sum_num + current_com
    command=input()
print(sum_num)
