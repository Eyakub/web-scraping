import xlrd


# open workbook
xl_workbook = xlrd.open_workbook('first_file.xlsx')

# get sheet by index
xl_worksheet = xl_workbook.sheet_by_index(0)

# find out the no of rows
rows = xl_worksheet.nrows

# read rows - row_values(row_number) return tuple
for row in range(rows):
    first_col, second_col = xl_worksheet.row_values(row)
    print(first_col, ' ', second_col)