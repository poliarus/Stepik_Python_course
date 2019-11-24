n = int(input('Enter number:'))
count1 = 1
count2 = 0
num_print = ()
globul_count = 0
while globul_count != n:
    num_print = count1
    while count2 < count1:
        count2 += 1
        print(num_print, end=' ')
        globul_count += 1
        if globul_count == n:
            break
        continue
    count1 += 1
    count2 = 0
