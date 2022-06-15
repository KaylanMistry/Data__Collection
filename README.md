# Data__Collection
This is a repository containing my code to scrape the website: https://www.fishwatch.gov/

Below displays the steps I took and the goals I achieved during this project.

Milestone 1:

Initially, my task was to find a website that firstly, I was interested in, and secondly that was set up to be scraped. 
I decided on the website 'Fishwatch' due to my love of animals. Additionally, the data shown on the website could be useful grouped and displayed in a table format which is why I proceeded with this website.

Milestone 2:

In this milestone I created a Scraper class to create methods to extract the data from the website 'Fishwatch'
This included methods to bypass cookies and simpler methods to scroll the website or click a next button.
Finally, as the aim of this scraper was to gather all the information of each item, I created a procedure to extract the links for each individual item.
Within the initialiser if__name__ = "__main__" block, I had my class call all the methods I had created, to ensure these methods were only run if the file is run directly rather than on an import.

Milestone 3:

Through this milestone I gave each product its own unique ID. Using the product's URL, I split this and labelled each Fish by its individual name, adding each name to a dictionary. 
Using version 4 UUID, I created a unique ID for each of these Fish, adding it the same dictionary along with their unique name.
After this I created methods to extract all the information and images from the Fish's page. As I wanted all the information to be readable and labelled, I created individual methods for each section of the page. Adding this the dictionary along with the unique ID's, created a separate section for each Fish and their own values.
As I could need this information at some point in time, I create a folder called raw_data and made sure I could store the Fish's data inside this directory. I saved the files as data.json.
As it is useful to have the images of each fish, I extracted the .png links for each fish, downloaded and stored them in a separate folder called 'images'. Using the name from each individual URL.

Milestone 4:

Refactoring and optimising code is essential to avoid nested loops or repeated code. The first step I completed within this milestone was to scrutinise my code and find any flaws.
Furthermore, for other people to understand my code, I added Docstrings to each method, clearly stating what the user required and how to use each method. 
Following this, I created a python document to test the methods as if they were to be used by the public. I needed to consider how to make the methods robust and guarantee I was obtaining all the information on each page.
I moved the if__name__ = "__main__" block onto the new file and tested this on the test.py document to make sure the files were organised and downloaded to the right places.

Milestone 5:

My next task was to upload all the individual fish's data onto an Amazon AWS S3 Bucket. Ideally, I would create a crawler to scrape the entire website, add each fish as independent json files to 'raw_data' and upload the entire folder using boto3.
However, at the end of testing I realised that the website structure was slightly different for the 'Farmed' fish, and they had swapped one 'U.S. Fishery' section to 'U.S. Farming'. This complicated my methods as I needed to create another method primarily for the 'Farmed' fish.
After constructing another method to suit the 'Farmed' fish, I decided to create a crawler to scrape the 'Wild' fish and edit this crawler to scrape the 'Farmed' fish. This way I wouldn't have repeated code and I could spend less time monitoring the crawler. 
Succeeding this task, I generated another RDS database and using pandas, I constructed and uploaded the tabular data to the new S3 bucket and well as the image data.

Milestone 6:

During this milestone, I made sure my scraper ran perfectly, adding features like tqdm to show visually how close the data was to be completely downloaded.
In addition, I finalised all public test methods and created a method to prevent the data from being rescraped using their unique ID.
After finding out I needed to run different crawlers, I created two different folders, one for 'Farmed' and another for 'Wild'.

Milestone 7:

In this section I converted all the data into tables using pandas and created another method to check the data within that table.
Following this I used two of the methods and created a Dockerfile which allowed me to build my scraper locally and test these methods in runs.
To add onto this, I made the scraper run on headless mode, and rebuilt the docker image consequently. 
As this was successful, I constructed the final docker image and push this onto my Dockerhub account. 
After this to confirm that the docker image didn't just run locally, I initiated an EC2 instance and built and ran the image onto there.

Milestone 8:

In this milestone I needed to set up a Prometheus container to run the scraper. To do this I needed to configure a prometheus.yml file and run the scraper in detach mode.
Next, I created a node exporter to monitor the hardware metrics when running the scraper locally and furthermore created a daemon.yml file to monitor the metrics of the container.
To see if the metrics were being sent, the website displayed if the nodes were 'UP' on the /targets page. Later once I sorted out the issues with these, I created a dashboard in Grafana to monitor the containers and hardware metrics of the EC2 instance.

Milestone 9:

To create a way to push a new image onto my Dockerhub account, in one action with commits, I needed to use GitHub Actions.
I did this by creating GitHub Secrets to create a Dockerhub Access Token and Dockerhub Username. Then linked this via GitHub Actions, and created steps to login, access and push the new image onto my Dockerhub account.
Using an EC2 scraper, I created cronjobs to stop the initial container I used and pull the latest docker image from my Dockerhub account.
