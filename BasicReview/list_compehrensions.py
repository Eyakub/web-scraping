"""
0   1   2   3   4
5   6   7   8   9
10  11  12  13  13
15  16  17  18  19
20  21  22  23  24
"""

# normal way
outter_list = []
for row in range(0, 25, 5):
    inner_list = []
    for column in range(row, row+5):
        inner_list.append(column)
    outter_list.append(inner_list)

print(outter_list)


# using list comphrensions
two_array = [[column for column in range(row, row+5)] for row in range(0, 25, 5)]
for row in two_array:
    print(row)