# Недавно мы считали для каждого слова количество его вхождений в строку (lesson66.py).
# Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто
# используемые.
# Напишите программу, которая считывает текст из файла (в файле может быть больше
# одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько
# раз оно встретилось. Если таких слов несколько, вывести лексикографически первое
# (можно использовать оператор < для строк).
# Слова, написанные в разных регистрах, считаются одинаковыми.

text = open("dataset_3363_3.txt", 'r')
l = text.read().replace('\n', ' ').lower().split()
text.close()

l.sort()
s = ''
c = 0
for i in l:
    if l.count(i) > c:
        s = i
        c = l.count(i)
print(s, c)
