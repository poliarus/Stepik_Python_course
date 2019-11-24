# Напишите программу, которая считывает с консоли числа (по одному в строке)
# до тех пор, пока сумма введённых чисел не будет равна 0 и сразу после этого
# выводит сумму квадратов всех считанных чисел.

# Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0,
# после этого считывание продолжать не нужно.

# В примере мы считываем числа 1, -3, 5, -6, -10, 13; в этот момент замечаем,
# что сумма этих чисел равна нулю и выводим сумму их квадратов, не обращая внимания на то,
# что остались ещё не прочитанные значения.

a = True
sum = 0
sum_q = 0
while a:
    n = int(input())
    sum += n
    sum_q += n * n
    if sum == 0:
        a = False
print(sum_q)
