from openpyxl import load_workbook
from openpyxl.drawing.image import Image

workbook=load_workbook(filename="c://data//demoopenxlwrite.xlsx")
sheet=workbook.active
logo=Image("c://data//download.JFIF")
logo.height=150
logo.width=150
sheet.add_image(logo, "D10")
workbook.save(filename="c://data//hclclogo.xlsx")