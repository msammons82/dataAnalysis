#Determine total number of rows
import openpyxl

path = " path of file"

wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active

print(sheet_obj.max_row)
