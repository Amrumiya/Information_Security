#!/usr/bin/python3
import datetime

with open("/home/youruser/logs.txt", "a") as f:
    f.write(f"Script ran at {datetime.datetime.now()}\n")

