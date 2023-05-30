import datetime

# User Defined Packages
from io_handler.Text_to_Speak import speak

def current_date():
    try:
        speak(datetime.date.today())
    except Exception as e:
        speak('An Error Occured')
        speak('Please Try Again')
        logging.error('An Error Occured...')