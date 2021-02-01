from PIL import Image
from PIL.ImageColor import getrgb
from PIL import ImageDraw

im1 = Image.open("So_Be_It_You_Nyun.png")

print(im1.size)

imN = Image.new(im1.mode,im1.size,color=getrgb("rgb(0,0,255)"))
draw = ImageDraw.Draw(imN)
p1 = im1.load()

yes=0
no=0

word = ""

toWrite = ""

for x in range(im1.size[0]):
    #print(x,d)
    for y in range(im1.size[1]):
        #print("("+str(x)+","+str(y)+") "+str(p1[x,y]))
        toWrite=toWrite+"\""+str(p1[x,y])+"\","
        r = p1[x,y][0]
        g = p1[x,y][1]
        b = p1[x,y][2]
        #if max(r,g,b)==r:
        draw.point((x,y),getrgb("rgb("+str(b)+",0,0)"))
##        elif max(r,g,b)==g:
##            draw.point((x,y),getrgb("rgb(0,255,0)"))
##        else:
##            draw.point((x,y),getrgb("rgb(0,0,255)"))
    toWrite+="\n"

imN.save("ranout.png","PNG")
##f=open("out.csv","w")
##f.write(toWrite)
##f.close()

print(yes,no)

print(word)

