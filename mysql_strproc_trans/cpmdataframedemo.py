import pandas as pd
import numpy as np
data1=pd.read_excel("c://data/myexcel.xlsx",sheet_name="Emp")
data2=pd.read_excel("c://data/myexcel.xlsx",sheet_name="Department")
print(data1)
print(data2)
data3=np.where(data1['Empid']==data2['Empid'],0,data2['Empid']-data1['Empid'])
print(data3)