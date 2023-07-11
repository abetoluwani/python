# File i/o is a method used to store names instead of typing it continually

# def main():
#     nameloop()
#
# def nameloop():
#     names = [] # empty list
#
#     for i in range(3):
#         # shorter and neater form to append multiple input
#         names.append(input("What is your name: "))
#
#
# # using the sorted funtion to sort the names alphabetically
#     for name in sorted(names):
#         print(f"Hello, {name}")
#
# if __name__ == '__main__':
#     main()

# File In Python
name = input("What is your name: ")

# file = open("names.txt","a")
# file.write(f"{name}\n")
# file.close()

# An alternative and pythonic way to the code above because it automatically close the file
with open("names.txt","a") as file :
    file.write(f"{name}\n")

with open("names.txt","r") as files:
    lines = files.readlines()
    line = sorted(lines) # sorting what's in the file before iterating over it

for j in line:
    # print("Hello,",line,end="") # First Method
    print("Hello,",j.rstrip()) #2nd rstrip() would strip off all new lines in the file