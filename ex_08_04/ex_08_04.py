fhand = open('romeo.txt')
words = []

for line in fhand:
    ws = line.rstrip().split()
    for w in ws:
        if w not in words:
            words.append(w)

words.sort()
print(words)