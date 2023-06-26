def whileloop():
    i = 3
    while i != 0:
        print("woof")
        i -= 1

    i = 1
    while i <= 3:
        print("hey")
        i += 1

    i = 0
    while i < 3:
        print("Dawg")
        i += 3

def forloop():
    number = 4
    for i in range(number ):
        print("dark")
def multiloop():
    print("Hey\n" * 3, end="")

def exloop():
    while True:
        n = int(input("What is n: "))

        if n <= 0:
            print("Invalid Number")
            continue
        else:
            break

    for i in range(n):
         print(n)

def main():
    whileloop()
    forloop()
    multiloop()
    exloop()

main()