

import os
from click import option
from requests import options
from selenium import webdriver
from sqlalchemy import false
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from tqdm import tqdm
from pathlib import Path
import time

import uuid
import urllib.request


import pandas as pd

MAX_FILES_PER_DIR = 106

myuuid = uuid.uuid4().hex

Individual_fishes = {}

data_complete = False

counter = False


url = []
Name = []
uuid_ = []

Fish_data = {'Image': [], 'AKA' : [], 'Basic_info' : [], 'Facts' : [], 'Fishery' : [], 'Science' : []}

Fish_data_farming = {'Image': [], 'AKA' : [], 'Basic_info' : [], 'Facts' : [], 'Farming' : [], 'Science' : []}

Fish = {'Name': [] , 'URL': [], 'UUID': [], 'Image': [], 'AKA' : [], 'Basic_info' : [], 'Facts' : [], 'Fishery' : [], 'Farming': [], 'Science' : []}


open_all_button = False

class Scraper:
    def __init__(self, fish, headless=False) -> None:

        self.fish = fish
        self.url = f'https://www.fishwatch.gov/profiles/{fish}'
        # s = ChromeDriverManager().install()
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-size=1024,768')
        if headless:
            options.add_argument('--headless')
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            # self.driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME, options=options)
            
        else:
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.url)
    
    def accept_cookies(self, xpath, iframe):
        '''
        This fuction allows the user to proceed through the 'Accept Cookies' screen, allowing
        the automation to access the webpage
        
        Public Use: User needs to add the Xpath for the iframe on the particular webpage to use this fucntion 
        
        '''
        try:
            time.sleep(2)
            self.driver.switch_to.frame(iframe)
            cookies_button = self.driver.find_element(By.XPATH, xpath)
            cookies_button.click()
        except:
            print('There was no cookies button')

    def click_search_bar(self, xpath):
        '''
        This function allows the automated system to click on the search bar.

        User needs to provide the Xpath for the search bar
        
        '''
        search_bar = self.driver.find_element(By.XPATH, xpath)
        search_bar.click()
        return search_bar

    def typing(self, xpath: str, text: str) -> None:
        '''
        Function to allows the automated system to insert text onto the webpage it is scraping.

        User needs to add the specified text, to use this function.
        
        '''
        search_bar = self.click_search_bar(xpath)
        search_bar.send_keys(text)

    def click_wild(self, xpath):
        wild_button = self.driver.find_element(By.XPATH, xpath)
        wild_button.click()
    
    def click_farmed(self, xpath):
        farmed_button = self.driver.find_element(By.XPATH, xpath)
        farmed_button.click()
        

    def click_fish(self, xpath):
        fishes = self.driver.find_element(By.XPATH, xpath) 
        fishes.click()
       
    def get_fish(self, class_name):
        '''
        This function captures the URL for each individual fish, and appends this to the 'Fish' dictionary.

        If another fish has been added to the database, + 1 to 115
        
        User needs to add the overall class name 'seafood profile'
        '''
        try:
            fishes_list = self.driver.find_elements(By.CLASS_NAME, class_name)
            fish_url = []
            for fish in fishes_list:
                link = fish.get_attribute('href')
                Fish['URL'].append(fish.get_attribute('href'))
                if len(fish_url) == 114:
                    pass
    
                else:
                    continue 
                
        except:
            print('Could not obtain Fish URLs')
            
        
        
    def get_id(self, class_name):
        '''
        This function captures the last part of each url, using this as a name for each fish.

        User needs to add the class the fish are under when introducing this fucntion, 'seafood-profile'.

        Also add +1 to 115 if another fish has been added to the database.
        
        '''
        try:
            new_data = self.driver.find_elements(By.CLASS_NAME, class_name)
            self.profile_name = []
            for fish in new_data:
                fish.get_attribute('href').rsplit('/')[-1]
                data = fish.get_attribute('href').rsplit('/')[-1]
                self.profile_name.append(data)
                # profile_name = data.text
                # Fish['Name'].append(data)
                Fish['Name'].append(fish.get_attribute('href').rsplit('/')[-1])
                if len(self.profile_name) == 114:
                    pass
                else:
                    continue
                [str(v) for v in Fish['Name']]
                return self.profile_name
        

        except:
            print('Could not obtain name for Fish')

    def get_uuid(self, length):
        '''
        This function generates a random UUID for each 'Fish' in the data base.

        User needs to add how many Fish are in the data base to access the function, and +1 to 115
        
        '''
        try:
            uuid_list = len(Fish['Name'])
            print(uuid_list)
            for i in range(107):
        
                # gen_uuid = uuid.uuid4()
                Fish['UUID'].append(uuid.uuid4().hex)
                if len(Fish['UUID']) == length:
                    pass

                else:
                    continue
                Fish['UUID'].append(uuid.uuid4().hex)
                
        except:
            print('Could not generate UUID for Fish')

    def click_fishes(self, xpath):
        try:
            fishes_container = self.driver.find_element_by_xpath(xpath) # Put this in after driver and all_profiles.click()
            fishes_list = fishes_container.find_elements_by_xpath('//section[@class="seafood-profiles"]//descendant::a')
            num_fishes = len(fishes_list)
            time.sleep(1)
            for i in range(num_fishes):
                fishes_container = self.driver.find_element_by_xpath('//section[@class="seafood-profiles"]')
                fish = fishes_container.find_elements_by_xpath('./a')[i]
                fish.click()
                this_url = self.driver.current_url
                # if this_url in df.values:
                #     print('This Object has already been scraped')
                #     counter = True
                #     pass
                # else:
                #     print('This Object has not been scraped')
                counter = False
                if counter == True:
                    bot.driver.back()
                time.sleep(2)
                bot.get_image('//figure[@data-profile-type="Wild"]')
                time.sleep(2)
                bot.get_aka('aka')
                time.sleep(1)
                bot.get_basic_info('//*[@id="overview"]')
                time.sleep(2)
                bot.get_facts('//section[@class="facts"]')
                time.sleep(2)
                bot.get_fishery_info('//a[@class="expand-toggle profiles-toggle"]') 
                time.sleep(2)
                
                bot.get_science_info('science')
                time.sleep(2)
                
                


                bot.driver.back()
                # bot.move_images('*.png')
        except:
            print('Could not click all fishes')

    def get_image(self, xpath): 
        '''
        This function obtains the image of the fish on the individual fishes' page.

        Needs to already be on the webpage of the fish you want to scrape for this function to work.

        User needs to add the Xpath of the figure the fish image is in.

        '''
        try:
            image_cont = self.driver.find_element(By.XPATH, xpath)
            image = image_cont.find_element_by_tag_name('img')
            image_link = image.get_attribute('src')
            self.image_data = [] 
            self.image_data.append(image_link)
            profile_name  = image.get_attribute('src').rsplit('/')[-1]
            downloaded_image = urllib.request.urlretrieve(image_link, profile_name)
            
            Fish['Image'].append(self.image_data)

            
        
        except:
            print('Could not obtain Fish Image')

    def get_images(self, xpath):
        image_cont = self.driver.find_element(By.XPATH, xpath)
        images_data = image_cont.find_elements_by_tag_name('img')
        image_lst = len(images_data)
        for i in range(image_lst):
            image_cont = self.driver.find_element_by_xpath('//a[@class="seafood-profile"]')
            image_data = image_cont.find_elements_by_tag_name('img')[i]
            images_link = images_data.get_attribute('src')
            self.images_data = []
        Fish['Image'].append(images_link)
        


    
          
    def get_aka(self, class_name): 
        '''
        This function obtains the Fish's name and appends this to 'Fish Data'.

        The name fo the class is 'aka' for each fish.

        Needs to already be on the webpage of the fish you want to scrape for this function to work.
        
        '''
        try:
            data = self.driver.find_elements(By.CLASS_NAME, class_name)
            aka_list = []
            for fish in data:
                
                fish.get_attribute('innerHTML')
                aka = aka_list.append(fish.get_attribute('innerHTML'))
                
                if len(aka_list) == 1:
                    pass
                else:
                    continue
                Fish['AKA'].append(aka_list)

        except:
            print('Could not obtain the AKA fish name')

    def get_basic_info(self, xpath):
        '''
        This function obtains the first section of the information, on the fishes' webpage.

        User needs to add the container 'overview' to access this function.

        Needs to already be on the webpage of the fish you want to scrape for this function to work.

        '''
        try:
            overview_cont = self.driver.find_element(By.XPATH, xpath)
            overview_list = overview_cont.find_elements_by_xpath('./a')
            data = []
            num_data = len(overview_list)

            for i in range(num_data):
                overview_cont = self.driver.find_element_by_xpath('//*[@id="overview"]')
                new_data = overview_cont.find_elements_by_xpath('./a')[i]
                overview = new_data.text
                data.append(overview)
            print(data)
            Fish['Basic_info'].append(data)

        except:
            print('Could not obtain "Basic information" of the Fish')

    def get_facts(self, xpath):
        '''
        This function scrapes the second section fo the Fish's database 'Facts'.

        User needs to add the Xpath of this section 'facts'.

        Needs to already be on the webpage of the fish you want to scrape for this function to work.

        '''
        try:
            facts_cont = self.driver.find_element(By.XPATH, xpath)
            facts_list = facts_cont.find_elements_by_tag_name('li')
            data = []
            num_facts = len(facts_list)

            for i in range(num_facts):
                facts_cont = self.driver.find_element_by_xpath('//section[@class="facts"]')
                new_data = facts_cont.find_elements_by_tag_name('li')[i]
                facts = new_data.text
                data.append(facts)
            Fish['Facts'].append(data)

        except:
            print('Could not obtain data from "Facts" ')    


    def get_fishery_info(self, xpath):
        '''
        This function clicks the open all button to allow the scraper to access all the relevent information.

        Then, it scrapes the third section on the Fish's page 'Fishery'.

        User needs to add the Xpath for the 'Open all' button to access this function.

        Needs to already be on the webpage of the fish you want to scrape for this function to work.
        '''
        try:
            open_all =  self.driver.find_element(By.XPATH, xpath)
            open_all.click()
            open_all_button = True
            time.sleep(0.7)
            
            fishery_cont = self.driver.find_element_by_id('fishery')
            fishery_data = fishery_cont.find_elements_by_xpath('//section[@id="fishery"]//descendant::li')
            new_data = []
            data = []
            fishery = []
            num_fishery = len(fishery_data)

            for i in range(num_fishery):
                fishery_cont = self.driver.find_element_by_id('fishery')         
                fishery_cont.find_elements_by_xpath('//section[@id="fishery"]//descendant::li')[i]
                new_data = fishery_cont.find_elements_by_xpath('//section[@id="fishery"]//descendant::li')[i]
                fishery = new_data.text
                data.append(fishery)
                
            Fish['Fishery'].append(data)

        except:
            print('Could not get "Fishery" information')
    
    def get_farming_info(self, xpath):
        '''
        This function clicks the open all button to allow the scraper to access all the relevent information.

        Then, it scrapes the third section on the Fish's page 'Farming'.

        User needs to add the Xpath for the 'Open all' button to access this function.

        Needs to already be on the webpage of the fish you want to scrape for this function to work.
        '''
        try:
            open_all =  self.driver.find_element(By.XPATH, xpath)
            open_all.click()
            open_all_button = True
            time.sleep(0.7)
            
            farming_cont = self.driver.find_element_by_id('farming')
            farming_data = farming_cont.find_elements_by_xpath('//section[@id="farming"]//descendant::li')
            data = []
            num_farming = len(farming_data)
            for i in range(num_farming):
                farming_cont = self.driver.find_element_by_id('farming')         
                new_data = farming_cont.find_elements_by_xpath('//section[@id="farming"]//descendant::li')[i]
                farming = new_data.text
                data.append(farming)
            Fish['Farming'].append(data)

        except:
            print('Could not get "Farming" information')


    def get_science_info(self, id):
        '''
        This function scrapes the fourth section on the Fish's page 'Science'.

        User needs to add the ID for the container for the Science section 'science'.

        Needs to already be on the webpage of the fish you want to scrape for this function to work.

        '''
        try:
            science_cont = self.driver.find_element(By.ID, id)
            science_data = science_cont.find_elements_by_xpath('//section[@id="science"]//descendant::li')
            data = []
            num_science = len(science_data)
            for i in range(num_science):
                science_cont = self.driver.find_element_by_id('science')
                new_data = science_cont.find_elements_by_xpath('//section[@id="science"]//descendant::li')[i]
                science = new_data.text
                data.append(science)
            Fish['Science'].append(data)

        except:
            print('Could not obtain data for the "Science" section')        

    def scroll(self, height):
        height = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight")
        time.sleep(2)
        self.driver.execute_script('window.scrollTo(0,' + str(height) + ');')
    
    def move_images(self, png):
        '''
        This function adds all the 'png' images to an 'Images__0' folder.

        User needs to type in '*.png' to activate this function.
        '''
        pngDirectory = Path()
        pngFiles = pngDirectory.glob(png)
        for pngFile in pngFiles:
            fileNumber = 1
            folderNumber = int(fileNumber / MAX_FILES_PER_DIR)
            currentFolder = pngDirectory / "Images__{}".format(folderNumber)
            if not currentFolder.exists():
                currentFolder.mkdir()

            pngFile.rename(currentFolder / pngFile.name)
    
    def check_data(self, url, uuid__):

        try:
            chosen_url = url
            chosen_uuid = uuid__
            
            if chosen_url in df.values:
                print('Value already in Dataframe')
                bot.driver.back()
            elif chosen_uuid in df.values:
                print('Value already in Dataframe')
                bot.driver.back()
            else:
                print('Value not in Dataframe')
                
        
        except:
            print('Could not complete data check')
    
    def get_images_(self):
        image_cont = self.driver.find_element_by_xpath('//section[@id="page"]')
        images_data = image_cont.find_elements_by_tag_name('img')
        image_lst = len(images_data)
        self.images_link = []
        for i in range(image_lst):
            image_cont = self.driver.find_element_by_xpath('//section[@id="page"]')
            image_data = image_cont.find_elements_by_xpath('//section[@id="page"]//img')[i]
            self.images_link.append(image_data.get_attribute('src'))
        self.images_link.pop()
        return self.images_link

    def downloaded_image(self, path='.'):
        if not os.path.exists(f'{path}/{self.fish}'):
            os.makedirs(f'{path}/{self.fish}')
        
        if self.images_link is None:
            print('No images found, please run get_images_() first')
            return None

        for i, scr in enumerate(tqdm(self.images_link)):
            print(scr)
            urllib.request.urlretrieve(scr, f'{path}/{self.fish}/{self.fish}_{i}.png')

    def get_basic_info_for_scraper(self):
        '''
        This function obtains the first section of the information, on the fishes' webpage.

        Needs to already be on the webpage of the fish you want to scrape for this function to work.

        '''
        try:
            overview_cont = self.driver.find_element_by_xpath('//*[@id="overview"]')
            overview_list = overview_cont.find_elements_by_xpath('./a')
            data = []
            num_data = len(overview_list)

            for i in range(num_data):
                overview_cont = self.driver.find_element_by_xpath('//*[@id="overview"]')
                new_data = overview_cont.find_elements_by_xpath('./a')[i]
                overview = new_data.text
                data.append(overview)
            print(data)
           
            return data

        except:
            print('Could not obtain "Basic information" of the Fish')       
       
        


if __name__ == '__main__':

    bot = Scraper("bluefish")
    time.sleep(0.5)
    time.sleep(2)


    bot.get_fish('seafood-profile')
    time.sleep(2)
    bot.get_id('seafood-profile')
    time.sleep(2)
    bot.get_images('//a[@class="seafood-profile"]')
    bot.get_basic_info_for_scraper

arrays = Fish['Name'], Fish['URL'], Fish['UUID'], Fish['Image'], Fish['AKA'], Fish['Basic_info'], Fish['Facts'], Fish['Fishery'], Fish['Farming'], Fish['Science']
max_length = 0
for array in arrays:
        max_length = max(max_length, len(array))

for array in arrays:
        array += ['NA'] * (max_length - len(array))

df = pd.DataFrame(Fish)
time.sleep(1)
print(df)
