

# def limit(exam_h, minimum=1, maximum=59):
#     return max(min(exam_h, maximum), minimum)
# exam_h=int(input("Hour of exam:"))
# 23 < exam_h >= 0
# 0 <= exam_h <=23

exam_h = int(input("Hour of exam:"))
while not (0 <= exam_h <= 23):
    exam_h = int(input("Hour of exam:"))

exam_m = int(input("Minute of exam:"))
while not (0 <= exam_m <= 59):
    exam_m = int(input("Minute of exam:"))

arrival_h = int(input("Hour of arrival:"))
while not (0 <= arrival_h <= 23):
    arrival_h = int(input("Hour of arrival:"))

arrival_m = int(input("Minute of arrival:"))
while not (0 <= arrival_m <= 59):
    arrival_m = int(input("Minute of arrival:"))

total_arrival=(arrival_h*60 + arrival_m)
total_exam=(exam_h*60+exam_m)

if total_exam - total_arrival > 30:
    print("Early")
    if total_exam-total_arrival < 60:
        print(f"{total_exam - total_arrival:02d} minutes before the start")
    elif total_exam - total_arrival >= 60:
        print(f"{(total_exam - total_arrival)//60}:{((total_exam-total_arrival)%60):02d} before the start")
elif total_arrival > total_exam:
    print("Late")
    if total_arrival - total_exam < 60:
        print(f"{abs(total_arrival-total_exam):02d} minutes after the start")
    elif total_arrival - total_exam >= 60:
        print(f"{(total_arrival-total_exam)//60}:{abs(((total_arrival-total_exam)%60)):02d} after the start")


elif total_exam - total_arrival <= 30 or total_exam - total_arrival ==0:
    print ("On time")
    if 0 < total_exam - total_arrival <= 30:
        print(f"{total_exam-total_arrival} minutes before the start")
# elif total_arrival > total_exam:
#     print("Late")
#     if total_arrival - total_exam < 60:
#         print(f"{abs(total_arrival-total_exam):02d} minutes after the start")
#     elif total_arrival - total_exam >= 60:
#         print(f"{(total_arrival-total_exam)//60}:{abs(((total_arrival-total_exam)%60)):02d} after the start")

