#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from colored import stylize, fg #for styling

print(stylize('------Current Ethereum Price------', fg('yellow')))
print(stylize('According to @coindesk.com', fg('red')))


class ScraperInfo:

    def __init__(self):
        self.url = "https://www.coindesk.com/price/ethereum"

    def __repr__(self):
        current_price = stylize(self.scrape(self.url), fg('yellow'))
        return f"Current Ethereum Price is: {current_price}$"

    def scrape(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        price = soup.find(class_='price-large')
        contents = [i for i in price]
        return contents[1]
        
if __name__ == "__main__":
    print(ScraperInfo())