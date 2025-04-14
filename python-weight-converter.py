# pythong weight converter

weight = float(input("Enter your weight: "))
unit = input("Choose a unit: (K or L): ")

if unit == "K" or unit =="k":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"your weight is {round(weight, 2)} {unit}")
elif unit == "L" or unit == "l":
    weight = weight/2.205
    unit = "Kgs."
    print(f"your weight is {round(weight, 2)} {unit}")
else:
    print(f"{unit} is invalid unit")
    
