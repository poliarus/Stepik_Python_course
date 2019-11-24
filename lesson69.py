# Чтение из файла
import os

inf = open('file.txt', 'r')  # open('file.txt)
s1 = inf.readline()
s2 = inf.readline()
inf.close()

# -----------------------------------------------
with open('text.txt') as inf:
    s3 = inf.readline()
    s4 = inf.readline()
# Здесь файл сам закроется

# Полезные функции
# s = inf.readline().strip()
# "\t abc \n".strip() --> 'abc'
# Убирает все служебные символы при чтении строки

os.path.join('.', 'dirname', 'filename.txt')
# './dirname/filename.txt'
