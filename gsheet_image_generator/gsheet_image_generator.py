import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from .gsheet_image import Create_service


class Image_generator(object):
    def __init__(self):
        print("Enter the Client Secret File")
        self.CLIENT_SECRET_FILE = str(input())
        self.API_SERVICE_NAME = 'drive'
        self.API_VERSION = 'v3'
        self.SCOPES = ['https://www.googleapis.com/auth/drive']
        self.service=Create_service(self.CLIENT_SECRET_FILE, self.API_SERVICE_NAME, self.API_VERSION, self.SCOPES)
        self.files_service=self.service.files()
        self.query_body="mimeType='application/vnd.google-apps.spreadsheet'"
        self.files_retrieved=self.files_service.list(
            q=self.query_body
        ).execute()
        self.drive_spreadsheet_files_data=pd.DataFrame(self.files_retrieved.get('files'))

        print(self.drive_spreadsheet_files_data.name)
        print("Enter the Respective Sheet Number to select the sheet : ")
        self.sheet_no=int(input())

        self.API_SERVICE_NAME = 'sheets'
        self.API_VERSION = 'v4'

        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
 
        self.spreadsheet_id=self.drive_spreadsheet_files_data.iloc[self.sheet_no]['id']
        self.service = Create_service(self.CLIENT_SECRET_FILE, self.API_SERVICE_NAME, self.API_VERSION, self.SCOPES)
        self.google_sheet = self.service.spreadsheets()
        self.rows = self.google_sheet.values().get(spreadsheetId=self.spreadsheet_id,range='Sheet1').execute()
        self.data = self.rows.get('values')
        self.df = pd.DataFrame(self.data)
        self.cols=self.df.iloc[0]
        self.df=self.df.iloc[1:]
        self.df.columns=self.cols

    def get_column(self,axis):
        print(self.df.columns)
        print("Enter the number to select the column for "+ axis +' axis')
        return str(input())

    def convert_timestamp_to_datetime(self):
        print(self.df.columns)
        print("Select & Enter column to convert it in to Date time")
        column=str(input())
        self.df[column]=self.df[column].astype('int')
        self.df[column]=self.df[column].apply(lambda x:pd.Timestamp(x,unit='s').date())
        self.df[column]=pd.to_datetime(self.df[column])
    
    def generate_year(self):
        print("Enter the column name from which you want to extract year")
        self.column_name=str(input())
        self.df['year']=self.df[self.column_name].dt.year
    def generate_month(self):
        print("Enter the column name from which you want to extract year")
        self.column_name=str(input())
        self.df['month']=self.df[self.column_name].dt.month

    def generate_day(self):
        print("Enter the column name from which you want to extract year")
        self.column_name=str(input())
        self.df['day']=self.df[self.column_name].dt.day

    def group_by_year(self):
        self.df=self.df.groupby(by=['year']).sum()
        self.df.reset_index(inplace=True)

    def group_by_month(self):
        self.df=self.df.groupby(by=['month']).sum()
        self.df.reset_index(inplace=True)

    def group_by_day(self):
        self.df=self.df.groupby(by=['day']).sum()
        self.df.reset_index(inplace=True)

    def plot_line_graph(self):
        self.df_cols=self.df.columns
        self.x_axis=self.get_column('X') #Selecting X-axis
        self.y_axis=self.get_column('Y') #Selecting Y-axis


        self.df[self.x_axis]=self.df[self.x_axis].astype('int')   #Converting the X-axis to Int
        self.df[self.y_axis]=self.df[self.y_axis].astype('int')   #Converting the Y-axis to Int
        plt.plot(self.df[self.x_axis],self.df[self.y_axis],'g')   #Plotting the Graph
        plt.yticks(np.linspace(0, max(self.df[self.y_axis])+1 , 10).astype('int'))          #Yticks for better vizulization
        plt.xticks(np.arange(min(self.df[self.x_axis]),max(self.df[self.x_axis]+1),1).astype('int'))  #Xticks for better vizulization
        plt.savefig(self.x_axis.capitalize()+"_vs_"+self.y_axis.capitalize()+"_Line_Graph")       #Saving the Graph as Image
        plt.show()

    def plot_bar_graph(self):
        self.df_cols=self.df.columns
        self.x_axis=self.get_column('X') #Selecting X-axis
        self.y_axis=self.get_column('Y') #Selecting Y-axis

        sns.barplot(self.df[self.x_axis],self.df[self.y_axis])   #Plotting the Graph 
        plt.savefig(self.x_axis.capitalize()+"_vs_"+self.y_axis.capitalize()+"_Bar_Graph")       #Saving the Graph as Image
        plt.show()

    def box_plot(self):
        self.df_cols=self.df.columns
        self.x_axis=self.get_column('X') #Selecting X-axis
        self.y_axis=self.get_column('Y') #Selecting Y-axis

        self.df[self.x_axis]=self.df[self.x_axis].astype('int')   #Converting the X-axis to Int
        self.df[self.y_axis]=self.df[self.y_axis].astype('int')   #Converting the Y-axis to Int

        sns.boxplot(x=self.df[self.x_axis],y=self.df[self.y_axis])   #Plotting the Graph 
        plt.savefig(self.x_axis.capitalize()+"_vs_"+self.y_axis.capitalize()+"_Box_plot")       #Saving the Graph as Image
        plt.show()

    def scatter_plot(self):
        self.df_cols=self.df.columns
        self.x_axis=self.get_column('X') #Selecting X-axis
        self.y_axis=self.get_column('Y') #Selecting Y-axis


        self.df[self.x_axis]=self.df[self.x_axis].astype('int')   #Converting the X-axis to Int
        self.df[self.y_axis]=self.df[self.y_axis].astype('int')   #Converting the Y-axis to Int
        plt.scatter(self.df[self.x_axis],self.df[self.y_axis],'*g')   #Plotting the Graph
        plt.yticks(np.linspace(0, max(self.df[self.y_axis])+1 , 10).astype('int'))          #Yticks for better vizulization
        plt.xticks(np.arange(min(self.df[self.x_axis]),max(self.df[self.x_axis]+1),1).astype('int'))  #Xticks for better vizulization
        plt.savefig(self.x_axis.capitalize()+"_vs_"+self.y_axis.capitalize()+"_Scatter_plot")       #Saving the Graph as Image
        plt.show()


    def plot_graph(self):
        print(" 1 -> For Line    Graph")
        print(" 2 -> For Bar     Graph")
        print(" 3 -> For Box     Plot ")
        print(" 4 -> For Scatter Plot ")
        num=int(input())
        if(num==1): 
            self.plot_line_graph()
        elif num==2:
            self.plot_bar_graph()
        elif num==3:
            self.box_plot()
        elif num==4:
            self.scatter_plot()
        else :
            print("The Number you Entered is wrong. Please Enter Correct Number and Try again.")

