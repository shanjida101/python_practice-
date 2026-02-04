#Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Is this weight in (K)g or (L)bs? ").upper()

if unit == 'K':
    weight = weight * 2.205
    unit = 'Lbs'
    print(f"Your weight in pounds is: {round(weight, 2)} {unit}")
elif unit == 'L':
    weight = weight / 2.205
    unit = 'Kg'
    print(f"Your weight in kilograms is: {round(weight, 2)} {unit}")
else:
    print(f"{unit} is an invalid unit.")
