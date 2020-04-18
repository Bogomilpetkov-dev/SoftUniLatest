user=input("Enter Username:")
password=input("Enter password:")

while password != "password":
    password=input("Enter password again:")

print(f"Welcome {user}!")