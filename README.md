# Data__Collection
This is a repository containing my code to scrape the website: https://www.fishwatch.gov/

Milestone 1:

Initially, my task was to find a website that firstly, I was interested in, and secondly that was set up to be scraped. 
I decided on the website 'Fishwatch' due to my love of animals. Additionally, the data shown in the website could be useful grouped and displayed in a table format which is why I proceeded with this website.

Milestone 2:

In this milestone I created a Scraper class to create methods to extract the data from the website 'Fishwatch'
This included methods to bypass cookies and simpler methods to scroll the website or click a next button.
Finally, as the aim of this scraper was to gather all the infirmation of each item, I created a procedure to extract the links for each individual item.
Within the initialiser 'if__name__ = "__main__"' block, I had my class call all of the methods I had created, to ensure it is only run if the file is run directly rather than on an import.

Milestone 3:

Through this milestone I gave each product its own unique ID. Using the product's URL, I split this and labelled each Fish by its individual name, adding each name to a dictionary. 
Using version 4 UUID, I created a unique ID for each of these Fish, adding it the the same dictionary along with their unique name.
After this I created methods to extract all the infromation and images from the Fish's page. As I wanted all the infromation to be readable and labelled, I created individaul methods for each section of the page. Adding this the the dictionary along with the unique ID's, created a separate section for each Fish and their own values.
As I could need this information at some point in time, I create a folder called raw_data and made sure I could store the Fish's data inside this directory. I saved the files as data.json.
As it is useful to have the images of each fish, I extracted the .png links for each fish, donloaded and stored them in a separate folder called 'images'. Using the name from each individual URL.

Milestone 4:

Refactoring and optimising code is essential to avoid nested loops or repeated code.  The first step I completed within this milestone was to scrutinise my code and find any flaws.

