from PIL import Image
from PIL.ImageColor import getrgb
from PIL import ImageDraw

im1 = Image.open("Color.png")

print(im1.size)

imN = Image.new(im1.mode,im1.size,color=getrgb("rgb(0,0,255)"))
draw = ImageDraw.Draw(imN)
p1 = im1.load()
yes=0
no=0

word = ""
for x in range(im1.size[0]):
    for y in range(im1.size[1]):
        if p1[x,y][:3]==(200,191,231):
            
            yes+=1
        else:
            no+=1
            draw.point((x,y),getrgb("rgb(255,0,0)"))

print(yes,no)

print(word)
imN.save("colorout.png","PNG")
