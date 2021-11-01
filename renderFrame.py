from PIL import Image
import color as c

def renderFrame(inFile, outDir, n, maxSize):

    #init vars
    img = Image.open(inFile)
    width, height = img.size
    out = ""

    #Rescaling if size is > max
    if width>maxSize or height>maxSize:
        img = img.resize((maxSize, maxSize))

    #Converting
    i=0
    while i<height:
        j=0
        while j<width:
            v = c.rgb_to_hsv(j, i, img)[2]
            if v>75:
                out = out+"  "
            elif v>50:
                out = out+"--"
            elif v>25:
                out = out+"=="
            else:
                out = out+"##"
            j=j+1
        out = out + "\n"
        i=i+1
    
    #filename
    filename = "00000"[0:-len(str(n))]+str(n)

    #Write to file
    f=open(outDir+f"/frame_{filename}.txt", "w+", encoding="utf8")
    f.write(out)
    f.close()