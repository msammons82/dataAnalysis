#program to extract number of columns
#need to install xlrd package

import xlrd

loc = ("path of file")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

sheet.cell_value(0, 0)

print(sheet.ncols)