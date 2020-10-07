# GSHEET_IMAGE_GENERATOR
## Use of this API

*__An awesome package which helps us in creating a graph from Google Sheets and stores them as an image.
The Graph is plotted by selecting two columns from the sheet i.e. for x-axis and y-axis.__*

## Installation
``` bash
pip install gsheet_image_generator
``` 

Log into the [Google Developers Console</u>](https://console.developers.google.com/) with the Google account whose
spreadsheets you want to access. Create (or select) a project and enable the
**Drive API** and **Sheets API** (under **Google Apps APIs**).

Go to the **Credentials** for your project and create **New credentials** > **OAuth client ID** > of type **Other**. In the list of your **OAuth 2.0 client IDs** click **Download JSON** for the Client ID you just created. Save the file as ``client_secrets.json`` in your home directory (user directory). Another file named ``storage.json`` in this example, will be created after successful authorization to cache OAuth data.

On your first usage of ``gsheet_image_generator`` with this file (holding the client secrets), your web browser will be opened, asking you to log in with your Google account to authorize this client read access to all its Google Drive files and Google
Sheets.

## How to use it?

### Step 1 
Open the Terminal and Run the below code to run the API.

``` python
gsheet_image_generator
```
### Step 2
After Running the above snippet you will asked to enter Google Sheet ID As Shown in the Below Image.

![1st](https://user-images.githubusercontent.com/35963631/95240319-da0e8c80-0829-11eb-9acd-896cde03dd47.png)

You can take below picture as reference to find the Sheet ID of a Google sheet.
<br></br>
The Sheet Id is Highlighted in Yellow Color.

![2nd](https://user-images.githubusercontent.com/35963631/95240395-f8748800-0829-11eb-8ed8-0da45cd62708.png)

### Step 3
After Entering the Sheet Id you will be able to see the below message if the permission to access the sheet has granted. Else you will see the Exception where your application failed.

![3rd](https://user-images.githubusercontent.com/35963631/95240457-104c0c00-082a-11eb-98a3-8aed817766fe.png)


## License

> This Package is licensed under the MIT license. See License for details.