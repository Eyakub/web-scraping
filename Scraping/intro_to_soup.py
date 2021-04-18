from bs4 import BeautifulSoup

def read_file():
    file = open('sample.html')
    data = file.read()
    file.close()
    return data


# make soup
# syntax = beautifulsoup(html_data, parser)
# Our parser is lxml or html.parser which we have installed

html_file = read_file()
soup = BeautifulSoup(html_file, 'lxml')

# access tag
meta = soup.meta

div = soup.div  # will return first div only
print(meta.get('charset'))

# tag methods
'''
attributes
.get() method
dictionary
'''

# Modify attributes
body = soup.body # first attributes of body
body['style'] = 'some style'    # setting value

title = soup.title
title.string.replace_with('title has been changed')
print(title)