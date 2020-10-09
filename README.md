# GSHEET_IMAGE_GENERATOR
## Use of this API

*__An awesome package which helps us in creating a graph from Google Sheets and stores them as an image.
The Graph is plotted by selecting two columns from the sheet i.e. for x-axis and y-axis.__*

--------
## Installation
```bash
pip install gsheet_image_generator
``` 

Log into the [Google Developers Console</u>](https://console.developers.google.com/) with the Google account whose
spreadsheets you want to access. Create (or select) a project and enable the
**Drive API** and **Sheets API** (under **Google Apps APIs**).

Go to the **Credentials** for your project and create **New credentials** > **OAuth client ID** > of type **Other**. In the list of your **OAuth 2.0 client IDs** click **Download JSON** for the Client ID you just created. Save the file as ``client_secrets.json`` in your home directory (user directory). Another file named ``storage.json`` in this example, will be created after successful authorization to cache OAuth data.

On your first usage of ``gsheet_image_generator`` with this file (holding the client secrets), your web browser will be opened, asking you to log in with your Google account to authorize this client read access to all its Google Drive files and Google
Sheets.

--------
## How to use it?

### Step 1 
Open the Terminal and Run the below code to run the API.
Pass the Path of the ``client_secrets.json`` while calling the ``Image_generator`` Class.

```python
>>> from gsheet_image_generator.gsheet_image_generator import Image_generator
>>> Ig=Image_generator(Path)
```

<br>After Running the above snippet you will see weather your request has granted or not, if granted then you will be asked to select the Spread Sheet from your `Google Drive`.</br>
<br> Select the respective number then the sheet will be Imported to your local computer.</br>

You can Inspect the Spread Sheet by running the below command after creating an Object for  `Image_generator()` class. 

```python 
>>> Ig.sheet.head()
```
---------

> If you want to convert a Data type of a column then use the below function.

```python
>>> Ig.convert_dtype(column, type_conversion)
```
The above function will take two arguments 1st is the column you want to convert and 2nd is Type to which you want to convert like('int', 'float' ,etc...)

---------
> If you want to convert a Timestamp column to DateTime then use the below function so that we can convert a timestamp dtype column to datetime dtype column.

```python
>>> Ig.convert_timestamp_to_datetime()
```
The above function will ask you you select a column from the Dataframe.

---------
> If you want to generate year column from datetime column in your Data frame then use the below function.

```python
>>>  Ig.generate_year()
```
---------
> If you want to generate month column from datetime column in your Data frame then use the below function.

```python
>>>  Ig.generate_month()
```
---------
> If you want to generate day column from datetime column in your Data frame then use the below function.

```python
>>>  Ig.generate_day()
```
---------
> If you want to group by entire Data frame on a particular column or liat of coluumns then use the below function.

```python
>>>  Ig.groupby_column(column)
```
The above function will take one argument i.e either a single column or a more than one column passed as a list.

## Generating Graphs as Images
--------
> If you want to plot a Line Graph and save it as an Image then Run the below commnad

```python
>>> Ig.plot_line_graph()
```
By Running the above command you will be asked to select two columns i.e. One For the X-axis and the other one for Y-axis And it will ask you to enter the Path where you want to store the Image on your local computer.

--------

> If you want to plot a Bar Graph and save it as an Image then Run the below commnad

```python
>>> Ig.plot_bar_graph()
```
By Running the above command you will be asked to select two columns i.e. One For the X-axis and the other one for Y-axis And it will ask you to enter the Path where you want to store the Image on your local computer.

--------

> If you want to plot a Box Plot and save it as an Image then Run the below commnad

```python
>>> Ig.box_plot()
```
By Running the above command you will be asked to select two columns i.e. One For the X-axis and the other one for Y-axis And it will ask you to enter the Path where you want to store the Image on your local computer.

--------
> If you want to plot a Scatter Plot and save it as an Image then Run the below commnad

```python
>>> Ig.scatter_plot()
```
By Running the above command you will be asked to select two columns i.e. One For the X-axis and the other one for Y-axis And it will ask you to enter the Path where you want to store the Image on your local computer.

## See also
--------
- [gsheets.py](https://pypi.org/project/gsheets/) - self-contained script to dump all worksheets of a Google
  Spreadsheet to CSV or convert any sub sheet to a pandas DataFrame (Python 2
  prototype for this library)
- [gspread](https://pypi.org/project/gspread/) - Google Spreadsheets Python API (more mature and featureful
  Python wrapper, currently using the XML-based `legacy v3 API`)

--------
## License

> This Package is licensed under the MIT license. See License for details.