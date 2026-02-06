name = input("What is your name? ")
#result = len(name)#print the length of the name
#result = name.upper()#convert the name to uppercase
#result = name.lower()#convert the name to lowercase
#result = name.capitalize()#capitalize the first letter of the name
#result = name.replace("a", "@")#replace all occurrences of "a" with "@"
#result = name.split()#split the name into a list of words
#result = name.strip("sha")#remove leading and trailing whitespace from the name
#result = name.startswith("S")#check if the name starts with "S"
#result = name.endswith("h")#check if the name ends with "h"
#result = name[0]#access the first character of the name
#result = name[1:4]#access a substring of the name from index 1 to 3
#result = name.find("h")#find the index of the first occurrence of "h"
#result = name.count("a")#count the number of occurrences of "a" in the name
#result = name.isalpha()#check if the name contains only alphabetic characters
#result = name.isdigit()#check if the name contains only digits
#print(result)

if len(name)>12:
    print("Your name is too long. Maximum length is 12 characters.")
if name.isspace():
    print("Your name cannot contain only spaces.")
if not name.isalpha():
    print("Your name must contain only alphabetic characters.")
elif not name.find(" ")== -1:
    print("Your name must not contain any space.")
else:
 print("Welcome, " + name + "!")
       