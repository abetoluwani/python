mystring = "I love programming\nand building apps and also writing ransomware "
print (mystring)
# indexing a string
car = mystring[:-10]
print(car)

# you cannot access a character and change it
# example = "Bunda"
# tryy = example[0]="P"
# print(tryy) # you would get an error

everyfirstchar = mystring[::1] #takes every first character
print(everyfirstchar)

every2ndchar =mystring[::2] #takes every second character
print(every2ndchar)

# reversing the string
reverse = mystring[::-1]
print(reverse)

# adding a variable to a string

name = "John Wick"
age = 4
moviename = f"The Name of the movie is {name} {age}"
print(moviename)

#uppercase
upper = mystring.upper()
print(upper)

#lower
lower = mystring.lower()
print(lower)

#capitalize
cap = mystring.capitalize()
print(cap)