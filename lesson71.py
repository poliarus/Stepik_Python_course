ouf = open('text.txt', 'w')
ouf.write('Some text\n')
ouf.write(str(25))
ouf.close()

# -------------------------
with open('text.txt', 'w') as ouf:
    ouf.write('Some text\n')
    ouf.write(str(25))
# Здесь файл уже закрыт
