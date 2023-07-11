# File i/o

def main():
    #name()
    nameloop()
def collname():
    nam = input("What's your name: ")
    print(f"hello,{nam}")

def nameloop():
    names = [] # empty list

    for i in range(3):
        name = input("What is your name: ")
        names.append(name)

    print(names)

if __name__ == '__main__':
    main()

