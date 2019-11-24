# Программе подаётся на вход число команд n, которые нужно выполнить черепашке,
# после чего n строк с самими командами. Вывести нужно два числа в одну строку:
# первую и вторую координату конечной точки черепашки. Все координаты целочисленные.
#  Sample Input:
# 4
# север 10
# запад 20
# юг 30
# восток 40
# Sample Output:
# 20 -20

l = []
for e in range(int(input())):
    l.append(input().lower().strip().split())

d = {}
key = ''
for i in range(len(l)):
    for j in l[i]:
        if not j.isdigit():
            key = j
            if key not in d:
                d[key] = []
        else:
            if not d[key]:
                d[key].append(int(j))
            else:
                x = int(d[key][0])
                x += int(j)
                d[key][0] = x

x = 0
y = 0
for key in d:
    if key == 'север':
        y += int(d.get(key)[0])
    elif key == 'юг':
        y -= int(d.get(key)[0])
    elif key == 'восток':
        x += int(d.get(key)[0])
    elif key == 'запад':
        x -= int(d.get(key)[0])

print(x, y)
