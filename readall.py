import os

path = "C:/Users/jUnio/Downloads/output/"
os.chdir(path)

def search():
    path = os.getcwd()
    l = os.listdir(path)
    for e in l:
        if os.path.isdir(e):
            os.chdir(e)
            search()
            os.chdir("..")
        else:
            f = open(e,"r")
            try:
                if "LBCTF" in f.read():
                    print(path+"\\"+e)
            except UnicodeDecodeError:
                g = open(e,"rb")
                print("lol")
            f.close()
        
search()
