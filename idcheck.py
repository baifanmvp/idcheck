import string

def idcheck(s):
    print "idcheck start!"
    letters = string.ascii_letters
    digits= string.digits
    s_l=len(s)
    
    if s_l >0 :
        if (s[0] in letters) == False and s[0] != "_":
            return False
        i=1
        while i < s_l:
            if (s[0] in letters) == False and s[0] != '_' and (s[0] in dights) ==False:
                return False
            i += 1
    return True

if __name__ == "__main__" :
    while True:
        s=raw_input(">")
        if idcheck(s) :
            print s, ": is  a id"
        else :
            print s, ": is not  a id"
