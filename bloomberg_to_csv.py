# Noel Caceres
# Bloomberg Quotes to CSV file

import requests
from bs4 import BeautifulSoup
import csv
import time

##  Scrape Bloomberg site quotes and write them to a Spreadsheet
def main():

    # bloomberg url quotes
    url = ['http://www.bloomberg.com/quote/SPX:IND',    # S&P 500
        'http://www.bloomberg.com/quote/INDU:IND',   # Dow Jones
        'http://www.bloomberg.com/quote/CCMP:IND']   # Nasdaq

    with open('bloomberg_quotes.csv','w') as quotes_file:
        writer = csv.writer(quotes_file)
        # write timestamp to csv
        writer.writerow([time.strftime('%Y'+'/'+'%m'+'/'+'%d '+'%X')])

        for i in url:
            soup = BeautifulSoup(requests.get(i).content, 'html.parser')

            # get instrument quote name and strip 
            name = soup.find('h1', attrs={'class':'name'}).text.strip()
            # get price
            price = soup.find('div',attrs={'class':'price'}).text.strip()

            # write name and price to csv
            writer.writerow([name, price])   

if __name__ == "__main__":
    main()
