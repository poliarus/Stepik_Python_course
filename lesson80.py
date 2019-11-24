import requests

url = ''
with open("dataset_3378_2.txt") as f:
    for line in f:
        url += line.strip()

r = requests.get(url)

with open('txt.txt', 'wt') as t:
    t.write(r.text)

lines = 0
for line in open('txt.txt'):
    lines += 1

print(lines)
