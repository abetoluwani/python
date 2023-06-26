# Exception in python (Also helps in error handling)
#try always works with an exception

while True:
    try:
        value = int(input("Enter x: "))
        print(f'x is {value}')

        if value == int(value):
            break
        else:
            continue
    except ValueError:
        print("x must be a number")