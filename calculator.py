num1= float(input("First Number: "))
num2 = float(input("Second Number: "))
operand = input("Operation ('*','/','+','-'): ")

if (operand == '+'):
    add = num1 + num2
    add = round(add,2)
    print(f"{add:,}") # adding comma to the result
elif (operand == '-'):
    sub = num1 - num2
    sub = round(sub,2)
    print(f"{sub:,}") # adding comma to the result
elif (operand == '/'):
    div = num1 /num2
    div = round(div, 2)
    print(f"{div:,}") # adding comma to the result
elif (operand == '*'):
    multi = num1 * num2
    multi = round(multi, 2)
    print(f"{multi:,}") # adding comma to the result
else:
    print("Invalid Operation Type")