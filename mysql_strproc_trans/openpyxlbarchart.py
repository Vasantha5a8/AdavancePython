from openpyxl.chart import BarChart,Reference
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
sales_data = [["ProductId","online","store"],[1,20,30],[2,40,50],[3,30,25],[4,35,45]]
for row in sales_data:
    sheet.append(row)
chart=BarChart()
data=Reference(worksheet=sheet,min_row=1,max_row=5,min_col=2,max_col=3)
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,"E2")
wb.save("c://data//chart.xlsx")
