import pandas as pd
d={'Team':["India","Austrlia","pakistan","Srilanka","england"],
   'Rank':[1,2,3,4,5],
   'Winper':['60%','55%','45%','35%','48%']
   }
df=pd.DataFrame(d)
#df.rename(columns={'Rank':'Ranking'},inplace=True)
#df.set_axis(df['Team'],inplace='True')#index based
print(df.loc)
print(df.iloc[[0,1],:])
#df.drop([0,2],axis=0,inplace=True)# rows printed
df.drop(['Winper'],axis=1,inplace=True)#cols printed
#print(df.loc[df['Ranking']>=3])
print(df)