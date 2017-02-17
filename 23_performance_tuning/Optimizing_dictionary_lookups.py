#import string and re
import string,re

allChar = string.ascii_uppercase + string.ascii_lowercase
"translates each character into the corresponding digit,"
"according to the matrix defined by maketrans."

charToSoundex =''.maketrans(allChar,"91239129922455912623919292" * 2 )

def soundex(source):
    "convert string toSoundex equivalent"

    #source string must to be at least 1 character and must consit entirely of letterss
    if ( not source) or ( not source.isalpha()):
        return "0000"

    #make first character uppercase
    #translate all other characters to soundex digits
    "translates"
    digits = source[0].upper() + source[1:].translate(charToSoundex)

    #remove consecutive duplicates
    digits2 = digits[0]
    for d in digits[1:]:
        if digits[-1] !=d:
            digits2 += d

    # remove all 9s with regular expression
    digits3 = re.sub('9','',digits2)

    #pad end with "0"s to 4 characters
    while len(digits3) < 4:
        digits3 +="0"

    #return first 4 characters
    return digits3[:4]

if __name__ == '__main__':
    from timeit import Timer
    names = ('A','Python','Programming')
    for name in names:
        statement = "soundex('%s')" % name
        t = Timer(statement, "from __main__ import soundex")
        print(name.ljust(15),soundex(name), min(t.repeat()))

        
