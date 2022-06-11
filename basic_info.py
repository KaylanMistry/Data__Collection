from Fishwatch import Scraper
import time

fish = input('Enter the name of the fish you want to scrape the basic infromation from: ')

my_scraper = Scraper(fish, headless=True)
my_scraper.get_basic_info_for_scraper()