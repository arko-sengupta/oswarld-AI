# Wiki Packages
import logging
import wikipedia

# User Defined Packages
from io_handler.Text_to_Speak import speak
from io_handler.Language_Model_1 import generate_two_word_token
from dependencies.Google import google_results


# Speak Details
def wiki_info(text):
    try:
        # Generate Two-Word Token
        text = generate_two_word_token(text)

        # Speak Searching Wikipedia
        speak('Searching Wikipedia...!')

        # Search on Google
        google_results(text)
 
        # Extract topic to fetch information
        text = text.replace('information','')

        # Content OSWARLD will speak
        content = wikipedia.summary(text, sentences=5)
    
        # Speak Content
        speak('According to Wikipedia!')
        speak(content)
    except Exception as e:
        speak('An Error Occured')
        speak('Please Try Again')
        logging.error('An Error Occured...')