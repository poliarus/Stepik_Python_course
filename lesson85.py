frm = input()
to = input()
si = input()
so = input()

print(si.translate(str.maketrans(frm, to)))
print(so.translate(str.maketrans(to, frm)))
