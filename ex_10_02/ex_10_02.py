fhand = open('mbox-short.txt')
dct = {}
for line in fhand:
    if line.startswith('From '):
        time = line.split()[5]
        hrs = time.split(':')[0]
        dct[hrs] = dct.get(hrs, 0) + 1

lst = sorted(dct.items())
for k, v in lst:
    print(k, v)