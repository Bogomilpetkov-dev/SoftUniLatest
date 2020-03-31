number = float(input("Enter number:"))
current_unit = str(input("Enter current unit:"))
wanted_unit = str(input("Enter wanted unit:"))

if current_unit == "mm" and wanted_unit == "cm":
    number = number * 0.1
    print(f'{number:.3f}')
elif current_unit == "mm" and wanted_unit == "m":
     number = number * 0.001
     print(f'{number:.3f}')
elif current_unit == "cm" and wanted_unit == "mm":
     number = number * 10
     print(f'{number:.3f}')
elif current_unit == "cm" and wanted_unit == "m":
     number = number * 0.01
     print(f'{number:.3f}')
elif current_unit == "m" and wanted_unit == "mm":
     number = number * 1000
     print(f'{number:.3f}')
elif current_unit == "m" and wanted_unit == "cm":
     number = number * 100
     print(f'{number:.3f}')


