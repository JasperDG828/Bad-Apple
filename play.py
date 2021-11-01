import os
import time

inDir = input("IN Directory > ")
files = os.listdir(inDir)
i=0

def clear():
    os.system("cls")

def start():
    global i
    while i<len(files):
        print(open(inDir+"/"+files[i]).read())
        time.sleep(0.03)
        
        i=i+1

start() 
