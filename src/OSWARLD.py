import tkinter as tk

# User Defined Packages
from io_handler.Voice_to_Text import voice_to_text
from io_handler.Text_to_Speak import speak
from dependencies.Introduction import Introduction
from dependencies.Wikipedia import wiki_info
from dependencies.Google import google_results
from dependencies.Youtube import youtube
from dependencies.Music import play_songs
from dependencies.Date import current_date

def process_command(input_command):
    if 'Introduction'.lower() in input_command.lower():
        Introduction()
    if 'Information'.lower() in input_command.lower():
        wiki_info(input_command)
    if 'Youtube'.lower() in input_command.lower():
        youtube(input_command)
    if 'Google'.lower() in input_command.lower():
        speak('Here are a few convenient results for you, Sir!')
        google_results(input_command)
    if 'Song'.lower() in input_command.lower():
        play_songs()
    if 'Date'.lower() in input_command.lower():
        current_date()

def text_input():
    console_output.insert(tk.END, 'Listening...\n')
    command = entry.get()
    process_command(command)


if __name__=='__main__':  
    # Create the main window
    window = tk.Tk()
    window.configure(bg="#001799")
    window.title("OSWARLD")
    
    # Create a label for instructions
    label = tk.Label(window, text="Let's Start", font=("Helvetica", 12, "italic"), fg="white", bg="navy", pady=10)
    label.pack(pady=(20, 0))
    
    # Create an entry field for user input
    entry = tk.Entry(window, font=("Helvetica", 12), width=30, bd=1, relief=tk.SOLID)
    entry.pack(pady=10)

    # Create a button to trigger the command
    button = tk.Button(window, text="Execute", command=text_input, font=("Helvetica", 10, "bold"), bg="navy", fg="white", padx=10, pady=5)
    button.pack(pady=(10, 0))

    # Create console output area
    console_output = tk.Text(window, height=10, width=40, bd=1,  font=("Helvetica", 12), borderwidth=1, relief=tk.SOLID)
    console_output.pack(pady=(20, 30), padx=30)
    
    # Start the main event loop
    window.mainloop()