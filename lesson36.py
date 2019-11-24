students = ['Ivan', 'Nik', 'Petya', 'Sasha', 'Olga', 'Boris', 'Sergey']

# Сохраниение отсортированной копии списка.
# Исходный список не изменяется!
ordered_students = sorted(students)
print(ordered_students)
print(students)

# Сортировка с сохранием изменений в исходном списке
students.sort()
print(students)

# Также к спискам можно применять функции min() и max(), при условии,
# что все элементы списка одного типа (числа, строки и т.д.).
# В противном случае эти функции вызовут ошибку!

students.reverse()  # Перевернуть исходный список
print(students)

print(students[::-1])  # Чтение списка к конца в начало
