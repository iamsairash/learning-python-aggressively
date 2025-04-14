# temperature converter

unit = input("Enter the unit: (F or C)")
temp = float(input("Enter your temperature: "))

if unit == "f" or unit == "F":
    temp = round(5/9 * (temp - 32), 2)
    unit = "C"
    print(f"your temperature is {temp}°{unit}")
elif unit == "C" or unit == "c":
    temp = round(9/5*temp + 32, 2)
    unit = "F"
    print(f"Your temperature is {temp}°{unit}")
else:
    print(f"{unit} is invalid unit")