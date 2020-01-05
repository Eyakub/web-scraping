from bs4 import BeautifulSoup


def read_file():
    file = open('sample.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(), 'lxml')

title = soup.body
parent = title.parent

# .parent
p = soup.p
print(p.parent.name)


# html
html = soup.html
print(type(html.parent))    # bs4 - html - 

# soup
print(soup.parent)