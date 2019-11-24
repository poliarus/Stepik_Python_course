# Двумерные списки

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(a)
print(a[1])
print(a[2][2])

# ------------------------------------
n = 3
a = [[0] * n] * n
print(a)

a[0][0] = 5
print(a)

a = [[0] * n for i in range(n)]
print(a)

a = [[1 for j in range(n)] for i in range(n)]
print(a)
