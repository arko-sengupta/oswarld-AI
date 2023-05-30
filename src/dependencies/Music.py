import os
import logging

# User defined Modules
from io_handler.Text_to_Speak import speak

def play_songs():
    try:
        # Configure the Directory
        music_dir = 'music_dir'
        songs = os.listdir(music_dir)
    
        for song in songs:
            os.startfile(os.path.join(music_dir, song))
        quit()
    except Exception as e:
        speak('An Error Occured')
        speak('Please Try Again')
        logging.error('An Error Occured...')