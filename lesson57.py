# Изменение объектов, связанных с локальными переменными


def append_zero(xs):
    xs.append(0)


a = []
append_zero(a)
print(a)  # [0]
