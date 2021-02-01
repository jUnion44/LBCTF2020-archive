from PIL import Image
from PIL.ImageColor import getrgb
from PIL import ImageDraw

im1 = Image.open("file.png")
im2 = Image.open("newfile.png")

print(im1.size==im2.size)

imN = Image.new(im1.mode,im1.size,color=getrgb("rgb(0,0,255)"))
draw = ImageDraw.Draw(imN)
p1 = im1.load()
p2 = im2.load()
p3 = imN.load()
yes=0
no=0

word = ""
for x in range(im1.size[0]):
    for y in range(im1.size[1]):
        if p1[x,y][:3]==p2[x,y][:3]:
            yes+=1
            #print("drawing")
            draw.point((x,y),getrgb("rgb(255,0,0)"))
        else:
            print("n")
            no+=1
            print(p1[x,y],p2[x,y])
            print(p2[x,y][2])
            #word += chr(p2[x,y][2])
            word += str(p2[x,y][2])

print(yes,no)

print(word)
imN.save("out.png","PNG")
