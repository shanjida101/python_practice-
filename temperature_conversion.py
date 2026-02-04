#convert temoperatures between Celsius, Fahrenheit, and Kelvin
unit = input("Enter the unit you want to convert from (C/F/K): ").upper()
temperature = float(input("Enter the temperature value: "))

if unit == 'C':
    fahrenheit = (temperature * 9/5) + 32
    kelvin = temperature + 273.15
    print(f"{temperature}°C is equal to {round(fahrenheit, 2)}°F and {round(kelvin, 2)}K")

elif unit == 'F':
    celsius = (temperature - 32) * 5/9
    kelvin = celsius + 273.15
    print(f"{temperature}°F is equal to {round(celsius, 2)}°C and {round(kelvin, 2)}K")

elif unit == 'K':
    celsius = temperature - 273.15
    fahrenheit = (celsius * 9/5) + 32
    print(f"{temperature}K is equal to {round(celsius, 2)}°C and {round(fahrenheit, 2)}°F")
else:
    print(f"{unit} is an invalid unit.")
