# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 20:31:22 2023

@author: rocki
"""

import psutil
import winsound
import time

def check_battery_level():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    
        
    if plugged:
        print("The laptop is plugged in.")
        if 75<percent<80:
            print(f"Battery level: {percent}%")
            time.sleep(60)
            check_battery_level()
        elif percent >= 80:
            print(f"Battery level: {percent}%")
            # Play alarm sound
            winsound.Beep(1000, 4000)  # Adjust the frequency (1000) and duration (2000) as needed
        
    else:
        if 25>percent>20 :
           print(f"Battery level: {percent}%")
           time.sleep(60)
           check_battery_level()
           # Play alarm sound
        if percent<=20:
           print(f"Battery level: {percent}%")
           winsound.Beep(1000, 4000) # Adjust the frequency (1000) and duration (2000) as needed 
        print("The laptop is running on battery.")

while True:
    check_battery_level()
    time.sleep(300)  # Check battery level every 5 minutes
