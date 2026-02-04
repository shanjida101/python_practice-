#python calculator operations

operation = input("Enter operation (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if operation == '+':
    result = num1 + num2
    print(result)
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {round(result)}") 

elif operation == '*': 
     result = num1*num2   
     print(f"{num1} * {num2} = {round(result,5)}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")                 
else:
    print(f"Invalid operation: {operation}")