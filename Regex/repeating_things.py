import re


# * character - this specifices that the previous character can be matched zero to infinity
regex = re.compile('a*')
print(regex.match('a'))
print(regex.match(''))


regex = re.compile('[a-c]*')
print(regex.match('aaaabaa'))


# * character from 0 to infinity, + character 1 to infinity
regex = re.compile('a+')
print(regex.match(''))

regex = re.compile('[a-c]+')
print(regex.match('abbd'))