from openpyxl import load_workbook
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]


wb = load_workbook(filename = 'URL\'s.xlsx')
ws = wb.active
#ws['B1'] = 101

allUrls = []
i = 1
currentUrl = ws['A1'].value

"""
while( currentUrl != None ):
    print( currentUrl )
    allUrls.append( currentUrl )
    i += 1
    currentUrl = ws[ 'A' + str(i) ].value
"""



creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("AnalyticaHouse").sheet1  # Open the spreadhseet


insertRow = ["hello", 5, "red", "from main file 2222"]
sheet.append_row( insertRow )