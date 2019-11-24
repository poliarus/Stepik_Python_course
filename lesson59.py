def print_value():
    print(a)
    a = 10
    print(a)


a = 5
print_value()
# UnboundLocalError: local variable 'a' referenced before assignment
# т.к. внутри функции используется локальная переменная "а", то программа считает,
# что функция обращается к ней. Но на момент вызова "а" еще не проинициализирована
