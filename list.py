from typing import Tuple, List, Any

mylist = ["banana","chery","apple"]
print(mylist)

# for empty list
mymtlist = list()
print(mymtlist)

# a list can allow a number , boolean and a string
alllist = [21, 232, 32, True, "name", "ER"]
print(alllist)

# you can assign a set of one list into one variable and print  
item = mylist [1] , mymtlist , alllist
print(item)

# to check there's something present in a list this works perfectly for restuarants and all
if "banana" in item:
    print("True")

else:
    print("Not Seen")

# cehcking how many elements are in a list
print(len(item))
# remove an element from the list
item = mylist.remove("banana")
print(item)

# remove all elements from a list
item = mylist.clear()
print(item)

# adding more values to the list
mymtlist.append ("lemon")
print(mymtlist)

# to insert an element into a particular index
mylist.insert(0,"drugs")
print(mylist)

# remove last  item from the list and print it out
item = mylist.pop()
print(item)

drugs = ["steroids","cocaine","xtc"]
# to reverse my list
rev = drugs.reverse()
print(drugs)

# to sort the list
rev = drugs.sort()
print(drugs)

# adding multiple list together
numb = [1,2,3,3,4]
alpha = ["a","b","c"]
intt = [12] * 5

ans = numb + alpha + intt

print(ans)

# slicing a list
new = [1,2,2,34,2,32,3232,33,242,4,42,]
print(new)
slic = new[:5]
print(slic)

slic = new[5:]
print(slic)

# to jump when slicing
jump = [1,2,2,34,2,32,3232,33,242,4,42,]
jum = jump[::4] # jumping over 4 variables
print(jum)
ju = jump[::2] # jumping over 2 variables
print(ju)

# instead of using the reverse here is also a nice way to reverse your list
juv = jump[::-1]
print(juv)

# to create a new list from an existing list
week =["monday","tuesday","wednesday","friday","saturady","sunday"]
weekend =week[-2:]
print(weekend)

num = [1,2,56,9,932,556,2,123,4,34,2,214,123]
squnum=[i*i for i in num]#creating a square of this list in another list
print(squnum)
div2 = [i/2 for i in num]# creating a division of 2
print(div2)
add = [i+5 for i in num] #adding 5 to every value for create the new set
print(add)

# more on list 
students = {
    #keys   #values
    "zsh": "shell",
    "github": "Version Control",
    "software": "Android Studio",
}

print(students["zsh"])
print(students["software"])
print(students["github"])

for i in students:
    print(i) # this would only print out the keys
    print(i, students[i])  # this would print out the keys and value

student = [
      #keys  #values
    {"zsh": "shell", "os": "debian","competitor":"powershell" },#dictionary
    {"github": "Version Control", "os": "Multiplatform", "competitor": "git , bitbucket"}, #dictionary
    {"software": "Android Studio", "os": "Android", "competitor": "Kotlin, React"},#dictionary
]

for i in student:
    print(f'{i["os"], i["competitor"]} \n')


