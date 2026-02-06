#format spacifiers = a way to format strings in python using placeholders
#placeholders are defined using curly braces {} and can be replaced with values using the format() method or f-strings
#{value:flags} format a value with specific flags to control the formatting
#flags can include width, precision, alignment, and type

price= 1999.990988
price2 =-3.14159


print(f"The price is: ${price:.2f}") #format price to 2 decimal places
print(f"The price is: ${price:10.2f}") #format price to 2 decimal places and set width to 10 characters
print(f"The price is: ${price:<10.2f}") #format price to 2 decimal places and left align within 10 characters
print(f"The price is: ${price:>10.2f}") #format price to 2 decimal places and right align within 10 characters
print(f"The price is: ${price:^10.2f}") #format price to 2 decimal places and center align within 10 characters
print(f"The price is: ${price:,.2f}") #format price to 2 decimal places and include comma as thousand separator
print(f"The price is: ${price2:010}") #format price2 as an integer with leading zeros and set width to 10 characters 
print(f"The price is: ${price:010}")  #format price as an integer with leading zeros and set width to 10 characters

print(f"The price is: ${price2:+}")