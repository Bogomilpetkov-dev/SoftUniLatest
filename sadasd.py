# # x=(input())
# #
# # revnumber=(str(x)[::-1])
# # print(revnumber)
#
# a=6
# b=3
# print(f"{a//b}")
#
# x=int(input())
#
# def reverse_integer(x):
#       sign = -1 if x < 0 else 1
#       x *= sign
#       # Remove leading zero in the reversed integer
#       while x:
#             if x % 10 == 0:
#                   # x /= 10
#             else:
#                   break
# print(sign)
#
# #       # string manipulation
# # #       x = str(x)
# # #       lst = list(x)  # list('234') returns ['2', '3', '4']
# # #       lst.reverse()
# # #       x = "".join(lst)
# # #       x = int(x)
# # #       return sign * x
# # #
# # #
# # # print(reverse_integer(x))
# # # # print(reverse_integer(-x))

# 23 < exam_h >= 0
# 0 <= exam_h <=23

exam_h = int(input("Hour of exam:"))
while 24 >= exam_h >=-1:
    exam_h = int(input("Hour of exam:"))