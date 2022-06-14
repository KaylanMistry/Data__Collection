# Data__Collection
This is a repository containing my code to scrape the website: https://www.fishwatch.gov/

Milestone 1:

Initially, my task was to find a website that firstly, I was interested in, and secondly that was set up to be scraped. 
I decided on the website 'Fishwatch' due to my love of animals. Additionally, the data shown on the website could be useful grouped and displayed in a table format which is why I proceeded with this website.

Milestone 2:

In this milestone I created a Scraper class to create methods to extract the data from the website 'Fishwatch'
This included methods to bypass cookies and simpler methods to scroll the website or click a next button.
Finally, as the aim of this scraper was to gather all the information of each item, I created a procedure to extract the links for each individual item.
Within the initialiser if__name__ = "__main__" block, I had my class call all the methods I had created, to ensure it is only run if the file is run directly rather than on an import.

Milestone 3:

Through this milestone I gave each product its own unique ID. Using the product's URL, I split this and labelled each Fish by its individual name, adding each name to a dictionary. 
Using version 4 UUID, I created a unique ID for each of these Fish, adding it the same dictionary along with their unique name.
After this I created methods to extract all the information and images from the Fish's page. As I wanted all the information to be readable and labelled, I created individual methods for each section of the page. Adding this the dictionary along with the unique ID's, created a separate section for each Fish and their own values.
As I could need this information at some point in time, I create a folder called raw_data and made sure I could store the Fish's data inside this directory. I saved the files as data.json.
As it is useful to have the images of each fish, I extracted the .png links for each fish, downloaded and stored them in a separate folder called 'images'. Using the name from each individual URL.

Milestone 4:

Refactoring and optimising code is essential to avoid nested loops or repeated code.  The first step I completed within this milestone was to scrutinise my code and find any flaws.
Furthermore, for other people to understand my code, I added Docstrings to each method, clearly stating what the user required and how to use each method.  
Following this, I created a python document to test the methods as if they were to be used by the public. I needed to consider how to make the methods robust and guarantee I was obtaining all the information on each page.
I moved the if__name__ = "__main__" block onto the new file an tested this on the test.py document to make sure the files were organised and downloaded to the right places.

Milestone 5:

My next task was to upload all the individual fish's data onto an Amazon AWS S3 Bucket.  Ideally I would create a crawler to scrape the entire website, add each fish as independant json files to 'raw_data' and upload the entire folder using boto3.
However, at the end of testing I realised that the website structure was slightly different for the 'Farmed' fish, and they had swapped one 'U.S. Fishery' section to 'U.S.Farming'.  This complicated my methods as I needed to create another method primarily for the 'Farmed' fish.
After constructing another method to suit the 'Farmed' fish, I decided to create a crawler to scrape the 'Wild' fish and edit this crawler to scrape the 'Farmed' fish.  This way I wouldn't have repeated code and I could spend less time monitoring the crawler. 
Succeeding this task, I generated another RDS database and using pandas, I constructed and uploaded the tabular data to the new S3 bucket and well as the image data.

