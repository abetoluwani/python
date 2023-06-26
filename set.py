# set are unordered and does not allow repeated values

myset = {1,2,2,4,1,2,3} # the set does not allow repeated element
print(myset)

# or we can use the set to create a set
myset2= set({1,3,4,"david",234})
print(myset2)

# the set is mutuable ; which allows adding of numbers
myset.add("david")
myset2.add("brigthon")
myset2.add("Bombal")
print(myset2)
print(myset)

# remove an element in  the set
myset2.remove("brigthon")
myset2.clear()

# to find an element in a set
newset = {1,2,"e",123,"dsjk"}

if 2 in newset:
    print("True")
else:
    print("False")

odds ={1,3,5,7,9}
even ={2,4,6,8,10}
prime = {2,3,5,7,11}

unite = odds.union(even) # combination of 2 sets together
print(unite)

inter = odds.intersection(even) # for intersection of 2 sets
print(inter) # it would be a null/empty set
inter1 = odds.intersection(prime)
inter2 = even.intersection(prime)
print(inter1) #{3, 5, 7}
print(inter2) # {2}

# to check out the elements in a set which is not in the other set
diff = even.difference(prime) # you should get {8, 10, 4, 6}
print(diff)
diff = prime.difference(even)
print(diff) #{11, 3, 5, 7}

# symmetric difference takes the different element from both sides
dif = even.symmetric_difference(odds)
print(dif) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

dif = odds.symmetric_difference(prime)
print(dif) #{1, 2, 9, 11}

# for elements found in  boths sets
odd ={1,3,5}
primee ={2,3,5}
odd.intersection_update(primee)
print(odd) # {3, 5}

set = {1,6,3,2,23}
print(set)