students = ['Ivan', 'Masha', 'Sasha']
teacher = ['Oleg', 'Alex']
print(students + teacher)

print([0, 1] * 4)

students[1] = 'Petya'  # Изменение элемента в списке
print(students)

students.append('Olga')  # Добавить элемент в конец списка
print(students)

students += ['Boris', 'Sergey']  # Добавление лементов в  конец списка
print(students)

students.insert(1, 'Nik')  # Вставка элемента (положение и элемент)
print(students)
