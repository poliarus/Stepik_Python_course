A = int(input("A: "))  # minimum
B = int(input("B: "))  # maximum
H = int(input("H: "))  # current

if A <= H <= B:
    print("Это нормально")
elif A > H:
    print("Недосып")
else:
    print("Пересып")
