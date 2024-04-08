import time

import bs4
import requests
import html
import json
from operator import itemgetter
from urllib.parse import unquote, quote

class RS3_Wiki_Page_Parser():
    def __init__(self):
        self.website_url_to_parse = ""
        self.website_to_parse = None
        self.parsed_website = None
        self.links_to_search = []
        self.exchange_wiki_api = "https://api.weirdgloop.org/exchange/history/rs/latest?name="
        self.prices = []
    def get_page_info(self, website_url_to_parse):
        self.website_url_to_parse = website_url_to_parse
        headers = headers = {
        'User-Agent': 'Category_Page_Based_Price_checker_scraper/0.1 (deathmunglar@gmail.com)'
        }
        try:
            self.website_to_parse = requests.get(website_url_to_parse, headers=headers)
            self.parsed_website = bs4.BeautifulSoup(self.website_to_parse.text, 'html.parser')
        except Exception as e:
            print(f"Could not connect to {website_url_to_parse} because of \n {e}")


    def get_GE_prices(self, max):
            if len(self.links_to_search) != 0:
                counter=1
                for item in self.links_to_search:
                    item_request = requests.get(item).json()
                    item_price =item_request[list(item_request.keys())[0]]['price']
                    if item_price < max:
                        self.prices.append([[list(item_request.keys())[0]],item_price])
                    print(f"percent complete {counter/len(self.links_to_search)*100:.2f}%")
                    counter+=1
                    time.sleep(0.5 *2)

    def get_elements_with_class(self,class_name):
        if self.parsed_website != None:
            divs =self.parsed_website.find_all(class_=class_name)
            for div in divs:
                links = div.find_all('a')
                for link in links:
                    self.links_to_search.append(self.exchange_wiki_api+quote( link.get("title")))

    def print_results(self):
        self.prices = sorted(self.prices,key=itemgetter(1))
        for items in self.prices:
            print(f"{items[0][0]} is currently at {items[1]:,}gp")