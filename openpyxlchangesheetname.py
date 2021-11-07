# import openpyxl module
import openpyxl

wb = openpyxl.Workbook()

sheet = wb.active
sheet.title = "sheet1"

print("sheet name is renamed as: " + sheet.title)