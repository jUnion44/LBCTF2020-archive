import random

def genKey():
	key = ""
	for i in range(9):
		key += chr(random.randint(33,126))
	return key
	
def impressKey(key):
	charList = list(key)
	impress = ""
	for char in charList:
		impress += (chr(abs(ord(char)-159)))
	return impress

IMPRESS = "lrZibDCbe"
KEY = "3-E6=[\\=:"

def getImpression():
        pos = list(range(33,127))
        pos = list(map(str,pos))
        for a in pos:
                print(a)
                for b in pos:
                        for c in pos:
                                for d in pos:
                                        for e in pos:
                                                for f in pos:
                                                        for g in pos:
                                                                for h in pos:
                                                                        for i in pos:
                                                                                if impressKey(a+b+c+d+e+f+g+h+i)=="lrZibDCbe":
                                                                                        print(a+b+c+d+e+f+g+h+i)

def enc(message, key):
	charList = list(message)
	cipherNums = []
	for i, char in enumerate(charList):
		cipherNums.append(str((((ord(char)^13)**2)/3)+ord(key[i%9])))
	return " ".join(cipherNums)
	
def dec(ciphertext, key):
        cipherNums = ciphertext.split(" ")
        charStr = ""
        for i, char in enumerate(cipherNums):
                toRev = float(char)
                print(toRev)
                toRev = toRev - ord(key[i%9])
                toRev = toRev * 3
                toRev = toRev ** (1/2)
                print(toRev)
                toRev = int(toRev)^13
                print(toRev)
                charStr = charStr + chr(int(toRev))
        return charStr


