# Напишите функцию modify_list(l), которая принимает на вход список целых чисел,
# удаляет из него все нечётные значения, а чётные нацело делит на два.
# Функция не должна ничего возвращать, требуется только изменение переданного
# списка, например:
# lst = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst))  # None
# print(lst)               # [1, 2, 3]
# modify_list(lst)
# print(lst)               # [1]
#
# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)               # [5, 4]
# Функция не должна осуществлять ввод/вывод информации.


def modify_list(l):
    # put your python code here
    i = len(l)-1
    while i != -1:
        if l[i] % 2 != 0:
            del l[i]
        elif l[i] % 2 == 0:
            l[i] //= 2
        i -= 1
    return

lst = [10, 5, 8, 3]
print(modify_list(lst))
print(lst)
