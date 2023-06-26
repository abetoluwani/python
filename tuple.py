# a tuple is created with parenthesis
# you cannot add an element in a tuple
data = ("Max",20,"chicago","data scientist")
print(data)

# to print out a particular element
part = data[1] , data [-1], data[0]
print(part)

# number of element in a tuple
print((len(part)))
# to count a specific thing in a tuple
print(data.count(20))

# finding the index of an element
print(data.index("Max")) #result is 0
print(data.index("chicago")) #result is 2

#reversing your tuple
rev = data[::-1]
print(rev)



