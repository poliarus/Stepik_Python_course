# Алгоритм Эвклида, для нахождения наибольшего общего делителя.
# Здесь мы находим наименьший делитель

a = int(input("a: "))
b = int(input("b: "))
c = a * b
while b:
    a, b = b, a % b
print(int(c / a))
