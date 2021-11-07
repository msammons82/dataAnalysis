#Adding style sheet in excel
import xlwt

workbook = xlwt.Workbook()

sheet = workbook.add_sheet("Sheet Name")

#Style
style = xlwt.easyxf('font: bold 1')

#specify column
sheet.write(0, 0, 'Sample', style)
workbook.save("sample.xls")