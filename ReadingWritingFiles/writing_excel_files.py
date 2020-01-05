from xlsxwriter import Workbook


# make workbook
workbook = Workbook('first_file.xlsx')

# add work sheet
worksheet = workbook.add_worksheet()

# write function - parameters -(row, column, value)
for row in range(20):
    worksheet.write(row, 0, 'row number')
    worksheet.write(row, 1, row)

# close workbook
workbook.close()