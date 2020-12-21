from GoogleImageScraper import GoogleImageScraper
import os

webdriver_path = os.getcwd()+"\\webdriver\\chromedriver.exe"
image_path = os.getcwd()+"\\photos"
#add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]
search_keys= ["brown among us character"]# , "red among us character", "lime among us character","brown among us character"]
number_of_images = 1
headless = False
#min_resolution = (width,height)
min_resolution=(0,0)
#max_resolution = (width,height)
max_resolution=(1920,1080)
for search_key in search_keys:
    image_scrapper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images,headless,min_resolution,max_resolution)
    image_urls = image_scrapper.find_image_urls()
    image_scrapper.save_images(image_urls)