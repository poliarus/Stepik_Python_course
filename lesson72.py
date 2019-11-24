import re
s = ''
with open('dataset_3363_2.txt') as inf:
    for line in inf:
        line = line.strip()
        g = re.findall("[a-zA-Z].[0-9]*", line)
        for i in g:
            i = i[0] * int(i[1:])
            s += i

with open('output.txt', 'w') as output:
    output.write(s)
