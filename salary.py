tabs = int(input("Opened tabs:"))
salary = int(input("Salary:"))
face_count = 0
insta_count = 0
reddit_count = 0

for count in range(0, tabs):
    website = input("name of website:")
    if website == "Facebook":
        face_count = face_count + 1
    if website == 'Instagram':
        insta_count = insta_count + 1
    if website == "Reddit":
        reddit_count = reddit_count + 1

    salary_final = salary - (face_count * 150 + insta_count * 100 + reddit_count * 50)

    if salary_final <= 0:
        print("You have lost your salary")
        break
if salary_final > 0:
    print(f"{salary_final}")
