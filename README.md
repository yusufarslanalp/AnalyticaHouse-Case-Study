# AnalyticaHouse-Case-Study

## URL of the Report
- https://docs.google.com/spreadsheets/d/1h3-mEsL-hyQw5o1vNQ8IT9rg2p9kVo4ou846q581QTw/edit?usp=sharing

## Used tech-stack
- BeautifulSoup: for scraping pages
- openpyxl: for reding xlsx file
- gspread: for writing data from python to Google Sheets

## Challenges
Lerning app script syntax. Google documentations are not good enough. 

## Benefits of project
- Learning web wscrapping in python
- Experiencing google-sheets and gooogle-apps-script
- Using copmarator function for custom sorts
- Lerning what exactly API is

## Answers of the additional questions

1) If I’d have 10.000 urls that I should visit, then it takes hours to finish. What can we make to fasten this process?

    We can use or multi threading or Async. With multi thread, tasks can be completed concurrently. With async, tasks can be completed pseudo concurrently. 

2) What can we make or use to automate this process to run once a day? Write your recommendations

    A python program can be implemented. A batch file or bash file can be placed to start-up folder. When computer starts up batch file run the python program.

    What does the python program:
        
        while( True ):
            if( todayAnUpdateNeeded() ):
                makeUpdate()
            sleep( 1 hour )

3) Please briefly explain what an API is and how it works.

    An application programming interface (API) is a connection between computers. An API has two parts. API specification and API implementation. API specification is a set of end points.

    Let say we have an online game. We have a score and we want to know our order among other users. And in the API specification there is an end point. The end point is: www.my-cool-game/oerder/{userID}. If ve make a request to the end poit the web server make a respond to us. Using the response we can learn our order.

    A set of end points like www.my-cool-game/oerder/{userID} and implementation of that and points creates an API.

## Missing Fİle
creds.json file does not pushed to repo. Because it includes private API Key.