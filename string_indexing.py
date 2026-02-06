#indexing = accessing individual characters in a string using their position (index)[start : end : step]

credit_card_number = "1234 5678 9012 3456"
print(credit_card_number[0])#access the first character of the string
print(credit_card_number[5])#access the sixth character of the string
 
print(credit_card_number[-1])#access the last character of the string
print(credit_card_number[-4])#access the fourth character from the end of the string

print (credit_card_number[0:4])#access the first four characters of the string
print(credit_card_number[5:9])#access characters from index 5 to 8
print(credit_card_number[0:16:2])#access every second character from index 0 to 15
print(credit_card_number[::-1])#reverse the string using slicing
print(credit_card_number[::2])#access every second character from the string