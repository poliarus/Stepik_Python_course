# СОХРАНЕНИЕ ПРИМЕРА НА БУДУЩЕЕ!!!

#  Sample Input:
# 3
# Зенит;3;Спартак;1
# Спартак;1;ЦСКА;1
# ЦСКА;0;Зенит;2

n = int(input())
d = {}
key = ''
for x in range(n):
    l = input()
    for i in l.split(';'):
        if l.split(';').index(i) % 2 == 0:
            key = i
            if key not in d:
                d[key] = list()
        else:
            d[key].append(int(i))

print(d)
