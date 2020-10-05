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
 
print("Enter Spread Sheet Id:- ")
spreadsheet_id=str(input())
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
    for column in df_cols:
        tk.Radiobutton(root, 
                      text=column[0].capitalize(),
                      indicatoron = 0,
                      width = 20,
                      padx = 20, 
                      variable=v, 
                      command=root.destroy,
                      value=column[1]).pack(anchor=tk.W)
    root.mainloop()
    return v.get()



def plot_graph():
    x_axis_column_index=get_column('X',df_cols) #Selecting X-axis
    x_axis=df_cols[x_axis_column_index][0]
    df_cols.pop(x_axis_column_index)
    y_axis_column_index=get_column('Y',df_cols) #Selecting Y-axis
    y_axis=df_cols[y_axis_column_index][0]


    df[x_axis]=df[x_axis].astype('int')   #Converting the X-axis to Int
    df[y_axis]=df[y_axis].astype('int')   #Converting the Y-axis to Int
    plt.plot(df[x_axis],df[y_axis],'g')   #Plotting the Graph
    plt.yticks(np.linspace(0, max(df[y_axis])+1 , 10).astype('int'))          #Yticks for better vizulization
    plt.xticks(np.arange(min(df[x_axis]),max(df[x_axis]+1),1).astype('int'))  #Xticks for better vizulization
    plt.savefig(x_axis.capitalize()+"_vs_"+y_axis.capitalize()+"_Graph")       #Saving the Graph as Image
    plt.show()

plot_graph()
print("Thanks For using this Library")


