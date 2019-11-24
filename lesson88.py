# Вычисление среднего роста учеников для классов

d = {x: [] for x in range(1, 12)}
key = ''
with open('dataset_3380_5.txt') as f:
    for line in f.readlines():
        for s in line.strip().split():
            if line.strip().split().index(s) == 0:
                key = int(s)
            else:
                d[key].append(s)

for key, value in d.items():
    av = 0
    for i in value:
        if i.isdigit():
            av += int(i)
    if not d[key] or len(value) == 0:
        print(key, '-')
    else:
        print(key, av/(len(value)/2))
