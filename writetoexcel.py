#writing to an excel sheet 
import xlwt
from xlwt import Workbook

wb = Workbook()

sheet1 = wb.add_sheet('Sheet 1')

sheet1.write(1, 0, 'New York')
sheet1.write(2, 0, 'South Carolina')
sheet1.write(3, 0, 'Florida')
sheet1.write(0, 1, 'States I lived in')

wb.save('xlwt example.xls')