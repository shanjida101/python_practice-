#while loop = executes a block of code as long as its condition is true
#break = used to exit a loop

name =input("What is your name? ")
 
while name == "":
     print("Please enter your name.")
     name = input("What is your name? ")
print("Hello, " + name + "!")


