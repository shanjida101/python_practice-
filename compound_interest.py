# Compound interest calculator 

principal =0
rate = 0
time = 0
while principal <= 0:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Principal amount must be greater than zero. Please try again.")
while rate <= 0:
    rate = float(input("Enter the annual interest rate (in %): "))
    if rate <= 0:
        print("Interest rate must be greater than zero. Please try again.")
while time <= 0:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time must be greater than zero. Please try again.")
interest = principal * (rate / 100) ** time
amount = principal + interest
#amount = principal * pow(1 + rate / 100, time)
print(f"The compound interest is: {round(interest, 2)}")
print(f"The total amount after {time} years is: {round(amount, 2)}")