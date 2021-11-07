#using indexing value for writing data in specific cells
import xlsxwriter

workbook = xlsxwriter.Workbook('Example2.xlsx')
worksheet = workbook.add_worksheet()

row = 0
column = 0

content = ["mike", "joseph", "sammons"]

for item in content:
    worksheet.write(row, column, item)
    row += 1

workbook.close()