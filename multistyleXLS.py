#adding multiple styles to a cell
import xlwt

workbook = xlwt.Workbook()

sheet = workbook.add_sheet("Sheet Name")

#applying multiple styles
style = xlwt.easyxf('font: bold 1, color red;')

sheet.write(0, 0, 'Sample', style)

workbook.save("sample.xls")