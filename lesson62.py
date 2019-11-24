# Set - множества

s = set()  # создание пустого множества

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print('orange' in basket)  # True
print('python' in basket)  # False

# Множества содержат только одну копию элемента. Повторяющиеся элементы не заносятся
#  во множества. Элементы хранятся в отсортированном виде

# Операции со множествами
element = ''
s.add(element)  # добавленние элемента
s.remove(element)  # удаление элемента. Если элемента нет, будет ошибка!
s.discard(element)  # удаление елемента, если он есть. Не вызывает ошибок!
s.clear()  # Удалить все элементы из множества
print()

for x in basket:
    print(x)
