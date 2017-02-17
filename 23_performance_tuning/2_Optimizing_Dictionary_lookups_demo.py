#import string and re
import string,re

charToSoundex = {"A":"9",
                 "B":"1",
                 "C":"2",
                 "D":"3",
                 "E":"9",
                 "F":"1",
                 "G":"2",
                 "H":"9",
                 "I":"9",
                 "J":"2",
                 "K":"2",
                 "L":"4",
                 "M":"5",
                 "N":"5",
                 "O":"9",
                 "P":"1",
                 "Q":"2",
                 "R":"6",
                 "S":"2",
                 "T":"3",
                 "U":"9",
                 "V":"1",
                 "W":"9",
                 "X":"2",
                 "Y":"9",
                 "Z":"2",}

"Wouldn't it be faster to write a loop checking each character"
isOnlyChars = re.compile('[A-Za-z]+$').search

def soundex(source):
    "convert string to Sountex equivalent"
    
    #source string must be at least 1 character and must consist enterely of letters
    if not isOnlyChars(source):
        return "0000"

    # make first character uppercase
    source = source[0].upper() + source[1:]

    #translate all other characters to Soundex digits
    digits = source[0]
    for s in source[1:]:
        s = s.upper()
        digits += charToSoundex[s]

    #remove consecutive duplicates
    digits2 = digits[0]
    for d in digits[1:]:
        if digits2[-1] !=d:
            digits2 += d

    #remove all "9"s
    digits3 = re.sub('9','',digits2)

    # pad end with "0"s to 4 characters
    while len(digits3) < 4:
        digits3 += "0"

    #return first 4 characters
    return digits3[:4]

if __name__ == '__main__':
    #import the class Timer from the module timeit
    from timeit import Timer
    names = ('A','Python','Programming')
    for name in names:
        statement = "soundex('%s')" % name
        t = Timer(statement,"from __main__ import soundex")
        print(name.ljust(15),soundex(name),min(t.repeat()))