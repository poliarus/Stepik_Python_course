# Вывести сумму всех нечетных чисел от a до b (включая обе границы) Вариант 1

a = int(input("a: "))
b = int(input("b: "))
s = 0

for i in range(a, b+1):
    if i % 2 != 0:
        s += i
print(s)
