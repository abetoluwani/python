name = input("What is your name: ").capitalize()

match name:
    case "Harry" | "Hermione" | "Ron" : #where | stands for the "or" operator
        print("Gryfindor")
    case "zab"|"Dave"|"Draco":
        print("Slytherin")
    case _: # Just like default in c or c++
        print("Who")
# match is an alternative to switch in switch in c and c++