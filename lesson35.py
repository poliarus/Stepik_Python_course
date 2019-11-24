students = ['Ivan', 'Nik', 'Petya', 'Sasha', 'Olga', 'Boris', 'Sergey']

students.remove('Sasha')  # Удаление элемента по значение. Удаляет только первое вхождение
print(students)  # Если элемента нет, выдаст ошибку

del students[1]  # Удаление элемента по индексу
print(students)

# Проверка и удаление элемента из списка

if 'Ivan' in students:
    print('Ivan is here')

if 'Anna' not in students:
    print('Anna is out')

ind = students.index('Olga')
print(ind)

# ind = students.index('Anna')  # ValueError: 'Anna' is not in list
# print(ind)
