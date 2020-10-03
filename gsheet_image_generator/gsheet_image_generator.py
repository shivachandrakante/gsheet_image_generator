import os
import numpy as np
import pandas as pd
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
plt.plot(df['year'],df['average_sales'],'g')
maxi=max(df.average_sales)
plt.yticks(np.linspace(0, maxi, 10).astype('int'))
plt.xticks(np.arange(min(df.year),max(df.year+1),1).astype('int'))
plt.savefig("year_vs_sales_graph")
plt.show()


