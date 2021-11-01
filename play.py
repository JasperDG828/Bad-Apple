import os
import time

inDir = input("IN Directory > ")
files = os.listdir(inDir)
files.sort()
i=0

def clear():
    os.system("clear")

def start():
    global i
    while i<len(files):
        print(open(inDir+"/"+files[i]).read())
        time.sleep(0.03)
        clear()
        i=i+1

start() 
