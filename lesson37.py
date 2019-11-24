# Если переменные ссылаются на один и тот же объект, то при изменение списка через
# переменную a, переменная b будет иметь такое же значение, т.к. фактически
# они ссылкаются на один и тот же объект
a = [1, 'A', 2]
b = a

a[0] = 42
print(a, b)

b[2] = 30
print(a, b)