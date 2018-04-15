http://gspread.readthedocs.io/en/latest/oauth2.html


Using Signed Credentials
1.  Head to Google Developers Console(https://console.developers.google.com/project) and create a new project (or select the one you have.)

2.  Under “API & auth”, in the API enable “Drive API”.

3.  Go to “Credentials” and choose “New Credentials > Service Account Key”.

4.  You will automatically download a JSON file with this data.

5.  In the next step you’ll need the value of client_email from the file.

Go to your spreadsheet and share it with a client_email from the step above. Otherwise you’ll get a SpreadsheetNotFound exception when trying to access this spreadsheet with gspread.
6. Install oauth2client:
    pip install --upgrade oauth2client
    
7. Now you can read this file, and use the data when constructing your credentials:


import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('gspread-april-2cd … ba4.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("Where is the money Lebowski?").sheet1


 4
down vote
accepted

Try to change your scope variable to the following:

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

Make sure Drive API is enabled in API console.

gspread has been upgraded and it's now based on API v4. It's faster but it requires updates in scope
