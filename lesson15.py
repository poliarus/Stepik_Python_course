# Сумма чисел от а до b

s = 0
a = int(input("начало: "))
b = int(input("конец: "))

while a <= b:
    s += a
    a += 1
print(s)
