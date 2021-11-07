#Determine total number of columns

import openpyxl

path = " path of file"

wb_obj = openpyxl.load_workbook(path)

sheet_obj = wb_obj.active
print(sheet_obj.max_column)
