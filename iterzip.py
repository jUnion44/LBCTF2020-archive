import zipfile, os

path = "C:/Users/jUnio/Downloads/output/"
os.chdir(path)

def search():
    path = os.getcwd()
    l = os.listdir(path)
    for e in l:
        print(e)
        if e == "The Answer is here.png":
            print(path+"\\"+e)
        if os.path.isdir(e):
            os.chdir(e)
            search()
            os.chdir("..")
        elif ".zip" in e:
            print(True)
            z=zipfile.ZipFile(e)
            z.extractall("arc "+e.split(",")[0])
            os.remove(e)
            print("ddddddd")
        
search()
