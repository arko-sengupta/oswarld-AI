import logging

# User defined Packages
from io_handler.Text_to_Speak import speak

def Introduction():
    try:
        # OSWARLD Opening
        speak('OSWARLD at you Service Sir!')

        # Will speak it's Introduction
        speak('My name is OSWARLD your own Desktop Assistant.')
        speak('I can perform certain activities for you like:')
        
        # List Activities
        # speak('Sending Quick Emails!')
        speak('Playing some Good Music for you!')
        speak('Can get you information about something you wanna know!')
        speak('Can Play Music on youtube as well!')
        speak('Can Search something on google for you!')
        speak('Can Tell you about the Weather report!')
        speak('Can Set alarm for you!')
        speak('Can open apps for you at your Local Environment!')
        speak('And More...')
    except Exception as e:
        speak('An Error Occured')
        speak('Please Try Again')
        logging.error('An Error Occured...')