# Напишите программу, которая выводит часть последовательности
# 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно).
# На вход программе передаётся положительное целое число n — столько элементов
# последовательности должна отобразить программа. На выходе ожидается последовательность
# чисел, записанных через пробел в одну строку.
# Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

n = int(input())
l = []
for i in range(n):
    for j in range(i):
        if len(l) < n:
            l.append(i)

for i in range(len(l)):
    print(l[i], end=' ')