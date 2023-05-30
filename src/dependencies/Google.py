# Automation Packages
import sys
import codecs
import requests
import logging
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# User Defined Packages
from io_handler.Text_to_Speak import speak
from io_handler.Language_Model_1 import generate_two_word_token

options = webdriver.ChromeOptions()
options.add_argument("--verbose")
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument("--window-size=1920, 1200")
options.add_argument('--disable-dev-shm-usage')

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# Search Keyword on Google
def google_results(text):
    try:
        # Generate Two-Word Token
        text = generate_two_word_token(text)

        # Speak Searching Wikipedia
        speak("Google is actually Great, Isn't it Sir...!")

        # Recognizing Browser
        driver = webdriver.Chrome(options=options)
    
        # Go to Google
        driver.get('https://www.google.com')
    
        # Locate the search box and enter the query
        search_box = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
        search_box.send_keys(text)
    
        # Press Enter to perform the search
        search_box.send_keys(Keys.RETURN)
    
        # Wait for the results to load
        time.sleep(5)
        response = driver.page_source
        response = response.encode('utf-8')
        soup = BeautifulSoup(response, "html.parser")
    
        # Find url in page
        wiki_urls = soup.find_all('a')
        wiki_urls = [wiki_url.get('href') for wiki_url in wiki_urls if wiki_url.get('href')]
        wiki_urls = [wiki_url for wiki_url in wiki_urls if 'https://en.wikipedia.org/wiki/' in wiki_url]
        
        # Go to the wiki page
        driver.get(wiki_urls[0])
        
        # Stay for OSWARLD to speak
        time.sleep(5)
    
        # Quit Driver
        driver.quit()
    except Exception as e:
        speak('An Error Occured')
        speak('Please Try Again')
        logging.error('An Error Occured...')