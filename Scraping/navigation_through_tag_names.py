from bs4 import BeautifulSoup


def read_file():
    file = open('sample.html')
    data = file.read()
    file.close()
    return data


soup = BeautifulSoup(read_file(), 'lxml')

# tag has many attributes
'''
tag.contents   - returns a list of children
'''
body = soup.body
for child in body.contents:
    # print(child if child is not None else '')
    pass


'''
tag.children - returns and iterator
'''
for child in body.children:
    print(child if child is not None else '')