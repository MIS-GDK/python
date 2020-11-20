import xlrd

print("1111")
data1 = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\111.xlsx")

# 查看工作表
data1.sheet_names()
print("sheets：" + str(data1.sheet_names()))
table = data1.sheet_by_name("Sheet1")
print("总行数：" + str(table.nrows))
print("总列数：" + str(table.ncols))
print("整行值：" + str(table.row_values()))
print("整行值：" + str(table.row_values(1)))
