a = float(input("a: "))
b = float(input("b: "))
c = input("operation ")

if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "/":
    if b != 0:
        print(a / b)
    else:
        print("Деление на 0!")
elif c == "*":
    print(a * b)
elif c == "mod":
    if b != 0:
        print(a % b)
    else:
        print("Деление на 0!")
elif c == "pow":
    print(a ** b)
elif c == "div":
    if b != 0:
        print(a // b)
    else:
        print("Деление на 0!")
