#install xlrd for use
#program to extract number of rows
import xlrd

loc = ("path of file")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)

print(sheet.nrows)