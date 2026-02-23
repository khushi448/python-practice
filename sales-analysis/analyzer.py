#--------for data-------
# import pandas as pd
# import json
# import os
# df=pd.read_csv('data/sales.csv')
# print("CSV DATA:")
# print(df)
# print(f"\nShape: {df.shape[0]} rows,{df.shape[1]} columns")
# df['Total']=df['quantity']*df['price']
# print(df)
# os.makedirs('output',exist_ok=True)
# df.to_json('output/sales_data.json',orient='records',indent=2)
# df.to_csv('output/sales_data.csv',index=False)
# df.to_excel('output/sales_data.xlsx',index=False)

#-------for helpers--------
# import pandas as pd
# from helpers import calculate_total,format_currency
# df=pd.read_csv('data/sales.csv')
# totals=[]
# for index,row in df.iterrows():
#   total=calculate_total(row['quantity'],row['price'])
#   totals.append(total)
# #add total to our data
# df['Total']=totals 
# print(df)
# # display with formatted total
# print ("sales data:")
# for index, row in df.iterrows():
#   formatted_total=format_currency(row['Total'])
#   print(f"{row['product']}:{formatted_total}")
# #show grand total
# grand_total=df['Total'].sum()
# formatted_grand_total=format_currency(grand_total)
#print(f"\nGrand total: {formatted_grand_total}")