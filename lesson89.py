import io

d = {}
f = io.StringIO("7	Ayrton	162\n"
"8	Enderson	168\n"
"6	Brickman	160\n"
"2	Bosworth	131\n"
"8	Higgins	161\n")

for line in f:
    print(line.strip().split())