# Реализация собственной функции min()

# a = [int(i) for i in input().split()]
a = [4, 7, 3, 8, 5, 9, 2, 1]
m = a[0]

for x in a:
    if m > x:
        m = x
print(m)
