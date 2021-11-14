from openpyxl import load_workbook
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from scrap import getProduct

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("AnalyticaHouse").sheet1  # Open the spreadhseet
fields = [ "URL", "Product Name", "Availability", "Offer", "Sale Price", "Product Price", "Product Code" ]

def insertProduct( product, sheet ):
    productRow = [ 
                    product.url,
                    product.productName,
                    "%" + str( product.availability ),
                    product.offer,
                    product.salePrice,
                    product.productPrice,
                    product.productCode
                ]
    #print( productRow )
    sheet.append_row( productRow )



wb = load_workbook(filename = 'URL\'s.xlsx')
ws = wb.active
#ws['B1'] = 101

allUrls = []
i = 1
currentUrl =  ws['A1'].value


while( currentUrl != None ):
    #print( currentUrl )
    allUrls.append( "https://www.markastok.com" + currentUrl )
    i += 1
    currentUrl = ws[ 'A' + str(i) ].value




for i in range( 0, len( allUrls ) ):
    currentProduct = getProduct( allUrls[i] )
    currentType = currentProduct.productType
    if( currentType == "available-product" or currentType == "no-stock" ):
        insertProduct( currentProduct, sheet )




