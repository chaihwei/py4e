from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_1049864.html'
html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# retrieve all of the span tags
nums = list()
tags = soup('span')
for tag in tags:
    nums.append(int(tag.contents[0]))

print(sum(nums))