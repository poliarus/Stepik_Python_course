# Вывести сумму всех нечетных чисел от a до b (включая обе границы) Вариант 2

# a, b = (int(i) for i in input().split())

a = int(input("a: "))
b = int(input("b: "))
s = 0

if a % 2 == 0:
    a += 1

for i in range(a, b+1, 2):  # Бежим по диапазону с шагом 2
    s += i
print(s)
