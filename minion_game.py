import time
def is_vowel(word):
    return word.upper() in "AEIOU"

def minion_game(string):
    kevin = 0
    stuart = 0
    length = len(string)
    
    for i in range(length):
        if is_vowel(string[i]):
            kevin += length - i
        else:
            stuart += length - i

    if kevin > stuart:
        print "Kevin", kevin
    elif kevin == stuart:
        print "Draw"
    else:
        print "Stuart", stuart

t0 = time.time()
minion_game("string"*100000)
print('%.1f'%(time.time()-t0))