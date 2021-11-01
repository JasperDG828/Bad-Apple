import renderFrame
import os
import math

inDir = input("IN Directory > ")
outDir = input("OUT Directory > ")
maxSize = float(input("MAX Size > "))
files = os.listdir(inDir)
i=0

while i<len(files):
    percent = math.floor(i/len(files)*100)
    print(f"\033[96m[TOTAL {percent}%]\033[0m Converting {files[i]} to text")
    renderFrame.renderFrame(inDir+"/"+files[i], outDir, i, maxSize)
    i=i+1
print("\033[92m\033[1mDONE\033[0m")

