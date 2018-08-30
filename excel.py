import xlrd

file_location = "C:/Users/swatthakur/Desktop/RFI Network_TET.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
# print(sheet.max_rows)
# sheet.cell_value(0,0)
# sheet.cell_value(0,1)
# sheet.cell_value(1,0)
# print(sheet.nrows)
# print(sheet.ncols)
# print(sheet.ncols, sheet.nrows)
# for row,column in range(sheet.nrows, sheet.ncols):
# 	print(sheet.cell_value(row, 0), sheet.cell_value(0, column))	
# for column in range(sheet.ncols):
# 	print(sheet.cell_value(0,column))
#Print all values, iterating through rows and columns

column = sheet.ncols   # Number of columns

for row in range(0, sheet.nrows):    # Iterate through rows
    #print(' '*40,'\n')
    #print ('Row: %s' % row ,'\n')   # Print row number
    for col in range(0, sheet.ncols):  # Iterate through columns
        cell_obj = sheet.cell_value(row, col)  # Get cell object by row, col
        print(cell_obj, end = " | ")
    print()

	



 		