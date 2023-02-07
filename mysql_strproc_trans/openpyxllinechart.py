from openpyxl.chart import LineChart,Reference
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
sales_data = [["year","sales"],[2010,10000],[2011,90000],[2012,20000],[2013,250000],[2014,440000]]
for row in sales_data:
    sheet.append(row)
chart=LineChart()
data=Reference(worksheet=sheet,min_row=1,max_row=6,min_col=1,max_col=2)
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,"E2")
wb.save("c://data//linechart.xlsx")
