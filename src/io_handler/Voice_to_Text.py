import logging
import speech_recognition as sr

def voice_to_text():
    try:
        # Creating a recognizer object
        recognizer = sr.Recognizer()
    
        # Use the microphone as the audio source
        with sr.Microphone() as source:
            # Confirm Listening
            print('Listening....')
    
            # Adjust the wait time
            recognizer.pause_threshold = 10
            
            # Capture the audio
            audio = recognizer.listen(source)
        
        # Convert speech to text
        recognized_text = recognizer.recognize_google(audio, language='en-in')
        
        # return recognized text
        return recognized_text
    except Exception as e:
        logging.info('An Error Occured: ', e)