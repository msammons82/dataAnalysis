#create and write on excel file using xlsxwriter
import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')

worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hello..')
worksheet.write('B1', 'This')
worksheet.write('C1', 'Is')
worksheet.write('D1', 'It')

workbook.close()