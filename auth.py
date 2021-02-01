import sys

def choose(s):
    r = 0
    for c in s:
        r += ord(c)**8// 3
    return str(r // 20 // 40)[:5]

def check(s):
    su = 0
    for c in s:
        su += ord(c)
    return su

def main():
    if len(sys.argv) < 2:
        s = input("Enter a string: ")
    else:
        s = sys.argv[1] 

    try:    
        assert len(s) == 9 
        assert check(s) == 940
        assert int(choose(s)) == 61735
        print(f"LBCTF{{{s}}}")
    except AssertionError:
        print("Access Denied")

if __name__ == "__main__":
    main()
