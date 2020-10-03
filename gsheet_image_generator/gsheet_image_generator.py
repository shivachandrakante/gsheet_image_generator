import os
import numpy as np
import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
from gsheet_image import Image_generator
 
CLIENT_SECRET_FILE = 'credentials.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
 
spreadsheet_id='1SrZfvr2ee54r7HR1jGtAE9zHIj_Y-UzK9ok8bdwkpqc'
service = Image_generator(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)
gs = service.spreadsheets()
rows = gs.values().get(spreadsheetId=spreadsheet_id,range='Sheet1').execute()
data = rows.get('values')
df = pd.DataFrame(data)
cols=df.iloc[0]
df=df.iloc[1:]
df.columns=cols
df['timestamp']=df['timestamp'].astype('int')
df['average_sales']=df['average_sales'].astype('int')
df['offer_price']=df['offer_price'].astype('int')
df['timestamp']=df['timestamp'].apply(lambda x:pd.Timestamp(x,unit='s').date())
df['timestamp']=pd.to_datetime(df['timestamp'])
df['year']=df['timestamp'].dt.year
df=df.groupby(by=['year']).sum()
df.reset_index(inplace=True)

df_cols=[]
for i in range(0,len(df.columns)):
    temp=(df.columns[i],i)
    df_cols.append(temp)


def get_column(axis,df_cols):
    root = tk.Tk()
    v = tk.IntVar()
    v.set(0)  # initializing the choice, i.e 1st Column
    tk.Label(root, 
         text="""Choose """+axis+""" from the list""",
         justify = tk.LEFT,
         padx = 20).pack()
    for val, column in enumerate(df_cols):
        tk.Radiobutton(root, 
                      text=column,
                      indicatoron = 0,
                      width = 20,
                      padx = 20, 
                      variable=v, 
                      command=root.destroy,
                      value=val).pack(anchor=tk.W)
    root.mainloop()
    return v.get()

x_axis_column_index=get_column('X',df_cols)
x_axis=df_cols[x_axis_column_index][0]
df_cols.pop(x_axis_column_index)
y_axis_column_index=get_column('Y',df_cols)
y_axis=df_cols[y_axis_column_index][0]

plt.plot(df[x_axis],df[y_axis],'g')
maxi=max(df.average_sales)
plt.yticks(np.linspace(0, maxi, 10).astype('int'))
plt.xticks(np.arange(min(df.year),max(df.year+1),1).astype('int'))
plt.savefig("year_vs_sales_graph")
plt.show()


