

def calculation():

    ask = input("Which operation are you going to perform? Press 1 for Addition, 2 for Subtraction 3. Division 4. Multiplication\n")
    if ask == '1':
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        add = int(a + b)
        print(add)

    if ask == '2':
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        sub = int(a - b)
        print(sub)

    if ask == '3':
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        div = int(a / b)
        print(div)

    if ask == '4':
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        mul = int(a * b)
        print(mul)

calculation()