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
# from io_handler.Voice_to_Text import voice_to_text
from io_handler.Text_to_Speak import speak
from io_handler.Language_Model_1 import generate_two_word_token

options = webdriver.ChromeOptions()
options.add_argument("--verbose")
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument("--window-size=1920, 1200")
options.add_argument('--disable-dev-shm-usage')

# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# Search Keyword on Google
def youtube(text):
    try:
        # Generate Two-Word Token
        text = generate_two_word_token(text)
    
        # Speak Searching Wikipedia
        speak('You can stay back and enjoy the Song, Sir...!')
    
        # Recognizing Browser
        driver = webdriver.Chrome(options=options)
    
        # Prepare song link
        url = 'https://www.youtube.com/results?search_query=' + text.replace(' ', '+')
    
        # Go to Google
        driver.get(url)
    
        # Wait for the results to load
        time.sleep(5)
    
        # Get page response
        response = driver.page_source
        response = response.encode('utf-8')
        soup = BeautifulSoup(response, "html.parser")
    
        # Song url in page
        song_url = soup.find('a', id = 'video-title')['href']
        
        # Go to the Song page
        driver.get('https://www.youtube.com/' + song_url)
    
        # Stop the song
        while True:
            print('Wanna End...')
            stop = input()
            stop = generate_two_word_token(stop)
            if stop.lower() == 'yes':
                break
    
        # Quit Driver
        driver.quit()
    except Exception as e:
        speak('An Error Occured')
        speak('Please Try Again')
        logging.error('An Error Occured...')