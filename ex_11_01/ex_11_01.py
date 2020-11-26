import re

total = []
fhand = open('regex_sum_1049862.txt')
for line in fhand:
    lst = re.findall('[0-9]+', line)
    if len(lst) == 0:
        continue
    for num in lst:
        total.append(int(num))

print(sum(total))