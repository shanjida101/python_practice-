print("Hello, World!")
name = input("What is your name? ")
print("Nice to meet you, " + name + "!")

age = int(input("How old are you? "))#typecasting string to integer
if age < 18:
    print("You are a minor.")
print("your age is " + str(age)) 

print(type(age))
 
 #type cast convert variabl from one data type to another data type
 #str() int() float() bool() 

#LOGICAL OPERATORS or and not
# or at least one condition is true
# and all conditions must be true
# not = reverses the boolean value

is_student = input("Are you a student? (yes/no): ").lower() == 'yes'
has_id = input("Do you have a student ID? (yes/no): ").lower() == 'yes' 
if is_student and has_id:
    print("You are eligible for a student discount.")

#condition  ... X if condition else Y
is_raining = input("Is it raining? (yes/no): ").lower() == 'yes'
activity = "stay indoors" if is_raining else "go outside" 

