import logging
import pyttsx3

def speak(text):
    try:
        # Initialize the pyttsx3 engine
        engine = pyttsx3.init()
        
        # Set the properties of the voice
        # Speed of speech
        engine.setProperty('rate', 150)
    
        # Volume level
        engine.setProperty('volume', 0.8)
        
        # Speak the provided text
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        logging.error('An Error Occured: ', e)