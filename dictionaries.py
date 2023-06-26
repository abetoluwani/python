# Dictionary is a data type that is unordered and mutable, it consist of a collection of key value pair
dick = dict(name="John Stones",age="27", city="manchester")
dicck ={"name": "John Stones", "age": 27, "city":"manchester"} # or you can use this for ypur dictionary
print(dick)
print(dicck)

# to lookup an element in the dictionary
namee = dick["name"]
print(namee)
agge = dick["age"]
print(agge)

# adding to our dictionary NB: this would overwrite the existing value in the dictionary
dick["email"]="johnnstones21@maxu.com"
print(dick)

# deleting an element from the dictionary
del dick["name"]
print(dick)

