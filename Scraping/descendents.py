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

children = [child for child in body.contents if child != '\n']
print(children)


'''
tag.descendents -- return us all the children of the said tag --generator
'''
for index,child in enumerate(soup.head.descendants):
    print(index)
    print(child if child != '\n' else '\\n')