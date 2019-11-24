import requests

basic_url = 'https://stepic.org/media/attachments/course67/3.6.3/'
step = ''

with open("dataset_3378_3.txt") as f:
    for line in f:
        step += line.strip()

r = requests.get(step)
step = r.text

a = True
while a:
    req = requests.get(basic_url+step)
    step = req.text
    print(req.url)
    if step[:2] == 'We':
        with open('song.txt', 'wt') as t:
            t.write(step)
        a = False
        print('The end!')
