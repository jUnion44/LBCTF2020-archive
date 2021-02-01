import hashlib


alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nums = list(range(10))
specialChars = ["!","@","_","&"]

for a in alpha[0:5]:
    
    for b in alpha[0:5]:
        
        for c in alpha[12:17]:
            c = c.upper()
            for d in nums:
                
                d = str(d)
                for e in specialChars:
                    
                    for f in alpha[0:5]:
                        testString = a+b+c+d+e+f+"14"
                        if str(hashlib.sha256(bytes(testString,encoding="ascii")).hexdigest())=="aeeb5e4b1802bd5c788602a1f4b64f9d28c74d3dacb4f9d19dbeac9860d94771":
                            print(testString)


