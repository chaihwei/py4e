try:
    filename = input('Please input a filename: ')
except:
    print('Please input a valid filename.')
    quit()

fhand = open(filename)
for line in fhand:
    print(line.rstrip().upper())