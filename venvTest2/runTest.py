#exec(open("testing.py").read())

import datetime
import os
from pathlib import Path
import csv
current_time = datetime.datetime.now()
current_date = str(current_time.year) + "-" + str(current_time.month)

dirName = str(os.getcwd() + "/")
dirString = dirName + 'data'

testPath = Path(dirString).is_dir()

if testPath == False :
    print("Path does not exist...")
    print(f"Creating new directory at {dirString}...")
    os.mkdir(dirString)
    print("Directory created...")
    dirString = dirString + "/"

if Path(dirString).is_dir() :
    dirString = dirString + "/"
    # Check for month-year directory
    dayMonStr = str(current_date)
    dirString = dirString + dayMonStr
    print(dirString)
    
    if Path(dirString).is_dir() :
        print("This is a directory...")
        print("Checking for csv file...")
        dayMonthStr = str(current_date) + "-" +  str(current_time.day) + ".csv"
        dirString = dirString + "/" + dayMonthStr
        if Path(dirString).is_file() :
            print("This file already exists...")
            print("Appending record to csv file...")
            fields = ['temperature', 'humidity','timestamp']
            
        else :
            print("Creating file with headers...")
            fields = ['temperature', 'humidity','timestamp']
            with open(dirString, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames = fields)
                writer.writeheader()
                print()
                print()
                print("Headers have been set...")
                print("Execution finished...")
                print("Closing file...")
                
                print("Appending record to csv file...")
                # append the record to the csv file here...

        
        


    else : 
        print("This is not a directory...")
        print("Creating directory...")
        os.mkdir(dirString)
        print("Directory has been made...")
        # Check for csv file here.... can be used as a function. Implement a function
        print("Creating csv file...")
        dayMonthStr = str(current_date) + "-" +  str(current_time.day) + ".csv"
        dirString = dirString + "/" + dayMonthStr # <<< not the same var as dayMonStr
        fields = ['temperature', 'humidity','timestamp']
        with open(dirString, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames = fields)
            writer.writeheader()
            print()
            print()
            print("Headers have been set...")
            print("Execution finished...")

