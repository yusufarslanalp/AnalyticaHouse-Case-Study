from bs4 import BeautifulSoup
import requests

#print( "HEREEEEEE" )

html_text = requests.get( 'https://www.markastok.com/buratti-slim-fit-fermuarli-dik-yaka-erkek-mont-556b79000-siyah' ).text
#html_text = requests.get( 'https://www.markastok.com/navigli-outdoor-erkek-ayakkabi-5601953-siyah-beyaz' ).text

soup = BeautifulSoup( html_text, 'lxml' )

productName = soup.find( 'h1', class_="fl col-12 product-name" ).text.strip()
offer = soup.find( 'div', class_="detay-indirim" ).text
allPrices = soup.find( 'div', class_="fl priceLine" ).find_all( 'span' )

productPrice = allPrices[1].text
salePrice = allPrices[3].text

#print( soup )
print( productName )
print( offer )
print( productPrice )
print( salePrice )

#for price in allPrices: 
    #print( price.text )



