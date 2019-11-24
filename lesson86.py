# Простая проверка орфографии на совпадения символов. Если написанной строки или слова
# нет в словаре, значит ошибка в этом слове

a = {input().lower().strip() for x in range(int(input()))}
b = [input().lower().strip().split() for y in range(int(input()))]
c = {n for e in b for n in e}  # совмещение 2-х списков в один с преобразованием в set() для удаления дубликатов
d = {z for z in c if z not in a}    # отфильтровываем совпадения

for i in d:
    print(i)
