from bs4 import BeautifulSoup


def read_file():
    file = open('sample.html')
    data = file.read()
    file.close()
    return data

soup =  BeautifulSoup(read_file(), 'lxml')
body = soup.body

# contents - html
# print(soup.html.contents)


# .previous_sibling
print(body.previous_sibling.previous_sibling)