def main ():
    height = int(input("Height:"))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#"*(i+1)) # the expression (i) is to add one to 1 so as to make sure the pyramid doesn't start from zero

main()

name = input("What is your name: ")

# stops the compiler from stopping after the first whitespace in a string input
name = name.strip()

print(f"Hello {name}, it was nice meeting you ")