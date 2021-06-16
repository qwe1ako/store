import xlrd
import xlwt
wb=xlrd.open_workbook(filename=r"D:\daima\day11[excle表读取]\代码\day11\用户.xls",encoding_override=True)
st=wb.sheet_by_name("管理")#选项卡
rows=st.nrows#行
cols=st.ncols#列
#获取所有行
for row in range(rows):
    value=st.row_values(row)

#获取所有列
for col in range(cols):
    value=st.col_values(col)

for row in range(rows):
    for col in range(cols):
        value=st.cell_value(row,col)
        print(value,"\t",end="")
    print()