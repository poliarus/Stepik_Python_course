# функции с аргументами по умолчанию


def my_range(start, stop, step=1):
    res = []
    if step > 0:
        x = start
        while x < stop:
            res += [x]
            x += step
    elif step < 0:
        x = start
        while x > stop:
            res += [x]
            x += step
    return res

print(my_range(2, 5))
print(my_range(2, 15, 3))
print(my_range(15, 2, -3))
