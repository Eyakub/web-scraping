import re


# ? question mark -- says the previous character can either come once or not at all
regex = re.compile('a?b')   # min 0     max 1
# print(regex.match('abb'))
# print(regex.match('b'))


# (m, n) n and m are integer values -- this qualifier means there must be 
# at least m repetitions and at most n
# if cross the n, will show only n-th elements
regex = re.compile('a{2,4}')
# print(regex.match('aaaaa'))


# *{0,}     -- zero minimum to infinity, {2,} two minimum
regex = re.compile('a{2,}')
# print(regex.match('a'))


# ?{0,1}
regex = re.compile('a{0,1}')
print(regex.match('aaa'))