st = input("Form: ")

if st == "треугольник":
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    p = float(a + b + c) / 2
    S = float(p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(S)
elif st == "прямоугольник":
    a = float(input("a: "))
    b = float(input("b: "))
    print(a * b)
elif st == "круг":
    r = float(input("r: "))
    print(3.14 * r * r)
