def init_values():
    a = 100
    b = 200


init_values()
# print(a + b)  # локальные переменные функции. Не видны за ее пределами


def init_values():
    a = 100

a = 0
init_values()
print(a)


def init_values(a):
    a = 100

b = 0
init_values(b)
print(b)
