a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print(max(a, b, c))
print(min(a, b, c))
print(a + b + c - max(a, b, c) - min(a, b, c))
