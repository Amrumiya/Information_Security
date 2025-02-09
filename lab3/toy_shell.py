#!/usr/bin/env python3

import os
import time
from datetime import datetime

def list_items_older_than(date_input):
    try:
        # Parse the input date
        target_date = datetime.strptime(date_input, "%Y-%m-%d").timestamp()
        
        # Get the current directory items (files and folders)
        items = os.listdir('.')
        for item in items:
            # Get the modification time (since creation time is unreliable on Windows)
            item_mtime = os.path.getmtime(item)
            if item_mtime < target_date:
                # Determine if the item is a file or folder
                item_type = "Folder" if os.path.isdir(item) else "File"
                modification_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item_mtime))
                print(f"{item} ({item_type}, Last Modified: {modification_time})")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
    except FileNotFoundError:
        print("Error: File not found.")

def toy_shell():
    print("Toy Shell: List files and folders older than a given date (based on modification time)")
    print("Enter a date in the format YYYY-MM-DD or type 'exit' to quit.")
    while True:
        try:
            command = input("toy-shell> ").strip()
            if command.lower() == "exit":
                print("Exiting toy shell.")
                break
            list_items_older_than(command)
        except KeyboardInterrupt:
            print("\nUse 'exit' to quit the shell.")

if __name__ == "__main__":
    toy_shell()
