# Убрать все дубликаты чисел

l = [1, 2, 3, 1, 2, 3, 4, 4, 5, 7, 7, 7, 9]
d = []

for x in range(len(l)):
    for y in range(len(l)):
        if l[y] == l[x]:
            if l[y] not in d:
                d.append(l[y])
            else:
                continue

for i in range(len(d)):
    print(d[i], end=' ')
