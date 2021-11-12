from openpyxl import load_workbook

wb = load_workbook(filename = 'URL\'s.xlsx')
ws = wb.active
#ws['B1'] = 101

allUrls = []
i = 1
currentUrl = ws['A1'].value


while( currentUrl != None ):
    print( currentUrl )
    allUrls.append( currentUrl )
    i += 1
    currentUrl = ws[ 'A' + str(i) ].value

