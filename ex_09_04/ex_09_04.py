fhand = open('mbox-short.txt')
words = []
dic = {}

for line in fhand:
    if line.startswith('From '):
        wds = line.split()
        email = wds[1]
        words.append(email)

for em in words:
    dic[em] = dic.get(em, 0) + 1

bigcount = None
bigword = None
for k, v in dic.items():
    if bigcount == None or v > bigcount:
        bigcount = v
        bigword = k
print(bigword, bigcount)