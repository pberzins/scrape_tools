import requests
import pymongo
from bs4 import BeautifulSoup




"""
Write a function that scrapes a URL using `requests`
Stores the response content in a database.
If you have already scraped the URL,
return the stored content instead of scraping it again.
"""


#Start a Mongo Database 'Scraped', with collection 'Website'
mc = pymongo.MongoClient('mongodb://localhost:27017/')
scrape_db = mc['scraped']
sites_collection = scrape_db['websites']



def scrape_site(url: str):
    """ Takes in a url as a string
        If the url is already in the data base,
        Return the content of the URL
        If it is not in the data base,
        add it with {'url' : url... and 'data' : html data...}
        and Return the content
    """
    data1 = get_data_from_database(url)
    if data1 != None:
        return data1
    else:
        r = requests.get(url)
        data = r.content
        durka = {}
        durka['url'] = url
        durka['data'] = data
        sites_collection.insert_one(durka)
        return data


def get_data_from_database(url):
    """ takes in a url
        returns the data if it is in the database
        else returns none
    """
    cursor = sites_collection.find()
    for site in cursor:
        if site['url'] == url:
            return site['data']
    return None
