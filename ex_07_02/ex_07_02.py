try:
    fname = input('Please input a filename: ')
except:
    print('Please input a valid filename!')
    quit()

total = 0
count = 0
fhand = open(fname)

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        bpos = line.find(' ')
        total = total + float(line[bpos+1 : ])

print('Average spam confidence:', total / count)