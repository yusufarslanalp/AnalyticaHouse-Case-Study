from bs4 import BeautifulSoup
import requests

class Product:
    productType = ""
    url = ""
    productName = ""
    offer = 0
    productPrice = 0
    salePrice = 0
    availability = 0

def getPageType( soup ):
    noStockClass = "popupWin box productFunction popupHide priceAlertLink"

    if( soup.find( 'div', class_="detay-indirim" ) != None ):
        return "available-product"
    if( soup.find( 'a', class_=noStockClass ) != None ):
        return "no-stock"
    return "unknown-type"

# 'https://www.markastok.com/buratti-slim-fit-fermuarli-dik-yaka-erkek-mont-556b79000-siyah'
# 'https://www.markastok.com/navigli-outdoor-erkek-ayakkabi-5601953-siyah-beyaz'
def getProduct( url ):
    html_text = requests.get( url ).text
    soup = BeautifulSoup( html_text, 'lxml' )
    product = Product

    product.productType = getPageType( soup )

    if( product.productType == "no-stock" ):
        product.productName = soup.find( 'h1', class_="fl col-12 product-name" ).text.strip()
    
    if( product.productType == "available-product" ):
        product.productName = soup.find( 'h1', class_="fl col-12 product-name" ).text.strip()
        product.offer = soup.find( 'div', class_="detay-indirim" ).text
        allPrices = soup.find( 'div', class_="fl priceLine" ).find_all( 'span' )
        product.productPrice = allPrices[1].text
        product.salePrice = allPrices[3].text
    return product


p = getProduct( 'https://www.markastok.com/erkek-mont?ps=10' )
print( p.productType )


