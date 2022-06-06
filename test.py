

from Fishwatch import Scraper
import time

fish = input('Enter the name of the fish you want to scrape the image from: ')

my_scraper = Scraper(fish, headless=True)
my_scraper.get_images_()
my_scraper.downloaded_image()
