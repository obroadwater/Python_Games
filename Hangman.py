from random import*
from time import*
lex = []
with open('lexicon.txt', 'r') as newFile:
    for i in range(58110):
        hj = newFile.readline().lower()
        lex.append(hj)
lex.remove('cross-bun\n')
lex.append('sabot')
#print(len(lex))




for c in lex:
    if 'a' not in c and 'e' not in c and 'i' not in c and 'o' not in c and 'y' not in c and 'u' not in c:
        lex.remove(c)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m', 'n', 'o','p','q','r','s','t','u','v','w','x','y','z']


prb = {'a': 36651, 'b': 9047, 'c': 19909, 'd': 19367, 'e': 56003, 'f': 6876, 'g': 14299, 'h': 10402, 'i': 42631, 'j': 807, 'k': 3943, 'l': 26399, 'm': 12944, 'n': 34477, 'o': 29054, 'p': 14119, 'q': 870, 'r': 35208, 's': 41430, 't': 33934, 'u': 16500, 'v': 5130, 'w': 4127, 'x': 1391, 'y': 8349, 'z': 715}
amod = []
for i in prb:
    sub = 0
    while sub <= prb[i]:
        amod.append(i)
        sub+=1

vwls = []
for c in amod:
    if c == 'a' or c== 'i' or c == 'e' or c == 'o' or c =='u':
        vwls.append(c)

def thr(guess, wrd): #Guessing w/ three letters remaining
    y = 1
    opt = []
    sub = 0
    for i in wrd:
        if i in guess:
            # a b _
            if sub < len(wrd)-3:
                if i in guess and wrd[sub+1] in guess and wrd[sub+2] not in guess:
                    for c in delta:
                        mny = 0
                        if c[0:2] == i + wrd[sub+1] and c[2] not in guess and delta[c] > 150:
                            while mny < delta[c]:
                                opt.append(c[2])
                                mny += 1
            # a _ c
            if sub < len(wrd)-3:
                if i in guess and wrd[sub+1] not in guess and wrd[sub+2] in guess:
                    for c in delta:
                        mny = 0
                        if c[0] + c[2] == i + wrd[sub+2] and c[1] not in guess:
                            while mny < delta[c]:
                                opt.append(c[1])
                                mny += 1
            #_ b c
            if sub > 2:
                if i in guess and wrd[sub-2] not in guess and wrd[sub-1] in guess:
                    for c in delta:
                        mny = 0
                        if c[1:3] == wrd[sub-1] + i and c[0] not in guess:
                            while mny < delta[c]:
                                opt.append(c[0])
                                mny += 1
        sub+=1
    if len(opt) > 0:
        ltr = opt[randint(0,len(opt)-1)]
    else:
        ltr = ''
    return ltr

def pfx(guess, wrd):#Guessing when first letter revelaed
    ltr = ''
    y = 1
    # if starts in e _
    if 'e' in guess and 'e' in wrd:
        if wrd[0] == 'e':
            if 'x' not in guess:
                ltr = 'x'
            elif 'n' not in guess:
                ltr = 'n'
    # if stars in a _ 
    if 'a' in guess and 'a' in wrd:
        if wrd[0] == 'a':
            if 'n' not in guess:
                ltr = 'n'
    # if starts in o _
    if 'o' in guess and 'o' in wrd:
        if wrd[0] == 'o':
            if 'v' not in guess:
                ltr = 'v'
            elif 'b' not in guess:
                ltr = 'b'
            elif 'r' not in guess:
                ltr = 'r'
    # if starts in i _ 
    if 'i' in guess and 'i' in wrd:
        if wrd[0] == 'i':
            if 'n' not in guess:
                ltr = 'n'
            elif 'm' not in guess:
                ltr = 'm'
    # if starts in u _
    if 'u' in guess and 'u' in wrd:
        if wrd[0] == 'u':
            if 'n' not in guess:
                ltr = 'n'
    # if starts in q _
    if 'q' in guess and 'q' in wrd:
        if wrd[0] == 'q':
            if 'u' not in guess:
                ltr = 'u'
            elif 'a' not in guess:
                ltr = 'a'
    # if starts in w _
    if 'w' in guess and 'w' in wrd:
        if wrd[0] == 'w':
            if 'a' not in guess:
                ltr = 'a'
            elif 'i' not in guess:
                ltr = 'i'
    # if starts in r _
    if 'r' in guess and 'r' in wrd:
        if wrd[0] == 'r':
            if 'e' not in guess:
                ltr = 'e' 
    # if starts in t _
    if 't' in guess and 't' in wrd:
        if wrd[0] == 't':
            if 'r' not in guess:
                ltr = 'r'
            elif 'e' not in guess:
                ltr = 'e'
    # if starts in y _
    if 'y' in guess and 'y' in wrd:
        if wrd[0] == 'y':
            if 'e' not in guess:
                ltr = 'e'
            elif 'o' not in guess:
                ltr = 'o'
            elif 'a' not in guess:
                ltr = 'a'
    # if starts in p _ 
    if 'p' in guess and 'p' in wrd:
        if wrd[0] == 'p':
            if 'r' not in guess:
                ltr = 'r'
            elif 'a' not in guess:
                ltr = 'a'
    # if starts in s _ 
    if 's' in guess and 's' in wrd:
        if wrd[0] == 's':
            if 't' not in guess:
                ltr = 't'
            elif 'u' not in guess:
                ltr = 'u'
    # if starts in d _
    if 'd' in guess and 'd' in wrd:
        if wrd[0] == 'd':
            if 'e' not in guess:
                ltr = 'e'
            elif 'o' not in guess:
                ltr = 'o'
    # if starts in f _
    if 'f' in guess and 'f' in wrd:
        if wrd[0] == 'f':
            if 'o' not in guess:
                ltr = 'o'
            elif 'l' not in guess:
                ltr = 'l'
    # if starts in g _ 
    if 'g' in guess and 'g' in wrd:
        if wrd[0] == 'g':
            if 'r' not in guess:
                ltr = 'r'
            elif 'a' not in guess:
                ltr = 'a'
    # if starts in h _
    if 'h' in guess and 'h' in wrd:
        if wrd[0]  == 'h':
            if 'a' not in guess:
                ltr = 'a'
            elif 'o' not in guess:
                ltr = 'o'
            elif 'e' not in guess:
                ltr = 'e'
    # if starts in j _ 
    if 'j' in guess and 'j' in wrd:
        if wrd[0] == 'j':
            if 'u' not in guess:
                ltr = 'u'
            elif 'o' not in guess:
                ltr = 'o'
    # if starts in k _
    if 'k' in guess and 'k' in wrd:
        if wrd[0] == 'k':
            if 'i' not in guess:
                ltr = 'i'
            elif 'n' not in guess:
                ltr = 'n'
    # if starts in l _
    if 'l' in guess and 'l' in wrd:
        if wrd[0] == 'l':
            if 'i' not in guess:
                ltr = 'i'
            elif 'a' not in guess:
                ltr = 'a'
    # if starts in z _
    if 'z' in guess and 'z' in wrd:
        if wrd[0] == 'z':
            if 'e' not in guess:
                ltr = 'e'
            elif 'o' not in guess:
                ltr = 'o'
            elif 'a' not in guess:
                ltr = 'a'
    # if starts in x _
    if 'x' in guess and 'x' in wrd:
        if wrd[0] == 'x':
            if 'e' not in guess:
                ltr = 'e'
            elif 'y' not in guess:
                ltr = 'y'
            elif 'r' not in guess:
                ltr = 'r'
    # if starts in c _
    if 'c' in guess and 'c' in wrd:
        if wrd[0] == 'c':
            if 'o' not in guess:
                ltr = 'o'
            elif 'a' not in guess:
                ltr = 'a'
            elif 'h' not in guess:
                ltr = 'h'
    # if starts in _ v 
    if 'v' in guess and 'v' in wrd:
        if wrd[1] == 'v':
            while y != 0:
                ltr = vwls[randint(0,len(vwls)-1)]
                if ltr not in guess:
                    y = 0
    # if starts in b _
    if 'b' in guess and 'b' in wrd:
        if wrd[0] == 'b':
            if 'a' not in guess:
                ltr = 'a'
            elif 'e' not in guess:
                ltr = 'e'
            elif 'r' not in guess:
                ltr = 'r'
    # if starts in n _
    if 'n' in guess and 'n' in wrd:
        if wrd[0] == 'n':
            if 'e' not in guess:
                ltr = 'e'
            elif 'o' not in guess:
                ltr = 'o'
    # if starts in m _ 
    if 'm' in guess and 'm' in wrd:
        if wrd[0] == 'm':
            while y != 0:
                ltr = vwls[randint(0,len(vwls)-1)]
                if ltr not in guess:
                    y = 0
    return ltr

def pfx2(guess, wrd): # Guessing when second letter is revealed
    ltr = ''
    r = 1
    # if starts in _ e
    if 'e' in guess and 'e' in wrd:
        if wrd[1] == 'e':
            if 'r' not in guess:
                ltr = 'r'
            elif 'd' not in guess:
                ltr = 'd'
    # if stars in _ a 
    if 'a' in guess and 'a' in wrd:
        if wrd[1] == 'a':
            if 'c' not in guess:
                ltr = 'c'
            elif 'm' not in guess:
                ltr = 'm'
            elif 'p' not in guess:
                ltr = 'p'
    # if starts in _ o
    if 'o' in guess and 'o' in wrd:
        if wrd[1] == 'o':
            if 'c' not in guess:
                ltr = 'c'
    # if starts in _ i 
    if 'i' in guess and 'i' in wrd:
        if wrd[1] == 'i':
            if 'd' not in guess:
                ltr = 'd'
            elif 'm' not in guess:
                ltr = 'm'
            elif 'l' not in guess:
                ltr = 'l'
    # if starts in _ u
    if 'u' in guess and 'u' in wrd:
        if wrd[1] == 'u':
            if 's' not in guess:
                ltr = 's'
            elif 'b' not in guess:
                ltr = 'b'
    # if starts in _ q
    if 'q' in guess and 'q' in wrd:
        if wrd[1] == 'q':
            if 's' not in guess:
                ltr = 's'
            elif 'e' not in guess:
                ltr = 'e'
            elif 'a' not in guess:
                ltr = 'a'
    # if starts in _ w
    if 'w' in guess and 'w' in wrd:
        if wrd[1] == 'w':
            if 's' not in guess:
                ltr = 's'
            elif 't' not in guess:
                ltr = 't'
            elif 'a' not in guess:
                ltr = 'a'
    # if starts in _ r
    if 'r' in guess and 'r' in wrd:
        if wrd[1] == 'r':
            if 'p' not in guess:
                ltr = 'p'
            elif 't' not in guess:
                ltr = 't'  
    # if starts in _ t
    if 't' in guess and 't' in wrd:
        if wrd[1] == 't':
            if 's' not in guess:
                ltr = 's'
            elif 'a' not in guess:
                ltr = 'a'
    # if starts in _ y
    if 'y' in guess and 'y' in wrd:
        if wrd[1] == 'y':
            if 'h' not in guess:
                ltr = 's'
            elif 's' not in guess:
                ltr = 's'
    # if starts in _ p
    if 'p' in guess and 'p' in wrd:
        if wrd[1] == 'p':
            if 's' not in guess:
                ltr = 's'
            elif 'a' not in guess:
                ltr = 'a'
    # if starts in _ s
    if 's' in guess and 's' in wrd:
        if wrd[1] == 's':
            if 'a' not in guess:
                ltr = 'a'
            elif 'e' not in guess:
                ltr = 'e'
    # if starts in _ d
    if 'd' in guess and 'd' in wrd:
        if wrd[1] == 'd':
            if 'a' not in guess:
                ltr = 'a'
            elif 'i' not in guess:
                ltr = 'i'
            elif 'e' not in guess:
                ltr = 'e'
    # if starts in _ f
    if 'f' in guess and 'f' in wrd:
        if wrd[1] == 'f':
            if 'a' not in guess:
                ltr = 'a'
            elif 'o' not in guess:
                ltr = 'o'
            elif 'e' not in guess:
                ltr = 'e'
    # if starts in _ g
    if 'g' in guess and 'g' in wrd:
        if wrd[1] == 'g':
            if 'a' not in guess:
                ltr = 'a'
    # if starts in _ h
    if 'h' in guess and 'h' in wrd:
        if wrd[1]  == 'h':
            if 'c' not in guess:
                ltr = 'c'
            elif 's' not in guess:
                ltr = 's'
            elif 't' not in guess:
                ltr = 't'
    # if starts in _ j
    if 'j' in guess and 'j' in wrd:
        if wrd[1] == 'j':
            if 'e' not in guess:
                ltr = 'e'
            elif 'a' not in guess:
                ltr = 'a'
            elif 's' not in guess:
                ltr = 's'
    # if starts in _ k
    if 'k' in guess and 'k' in wrd:
        if wrd[1] == 'k':
            if 's' not in guess:
                ltr = 's'
    # if starts in _ l
    if 'l' in guess and 'l' in wrd:
        if wrd[1] == 'l':
            if 'f' not in guess:
                ltr = 'f'
            elif 'f' not in guess:
                ltr = 'c'
    # if starts in _ z 
    if 'z' in guess and 'z' in wrd:
        if wrd[1] == 'z':
            if 'a' not in guess:
                ltr = 'a'
            elif 'c' not in guess:
                ltr = 'c'
            elif 'o' not in guess:
                ltr = 'o'
    # if starts in _ x
    if 'x' in guess and 'x' in wrd:
        if wrd[1] == 'x':
            if 'e' not in guess:
                ltr = 'e'
            elif 'o' not in guess:
                ltr = 'o'
            elif 'a' not in guess:
                ltr = 'a'
    # if starts in _ c
    if 'c' in guess and 'c' in wrd:
        if wrd[1] == 'c':
            if 's' not in guess:
                ltr = 's'
            elif 'a' not in guess:
                ltr = 'a'
    # if starts in _ v
    if 'v' in guess and 'v' in wrd:
        if wrd[1] == 'v':
            if 'o' not in guess:
                ltr = 'o'
            elif 'e' not in guess:
                ltr = 'e'
            elif 'a' not in guess:
                ltr = 'a'
    # if starts in _ b
    if 'b' in guess and 'b' in wrd:
        if wrd[1] == 'b':
            if 'a' not in guess:
                ltr = 'a'
            elif 'o' not in guess:
                ltr = 'o'
    # if starts in _ n
    if 'n' in guess and 'n' in wrd:
        if wrd[1] == 'n':
            if 'i' not in guess:
                ltr = 'i'
            elif 'u' not in guess:
                ltr = 'u'
    # if starts in _ m
    if 'm' in guess and 'm' in wrd:
        if wrd[1] == 'm':
            if 'i' not in guess:
                ltr = 'i'
            elif 'e' not in guess:
                ltr = 'e'
    return ltr

def sfx(guess, wrd): #guessing when last letter is revealed
    ltr = ''
    y = 1
    # if ends in e _
    if 'e' in guess and 'e' in wrd:
        if wrd[len(wrd)-2] == 'e':
            if 'l' not in guess:
                ltr = 'l'
            elif 't' not in guess:
                ltr = 't'
    # if ends in _ a 
    if 'a' in guess and 'a' in wrd:
        if wrd[len(wrd)-2] == 'a':
            if 'i' not in guess:
                ltr = 'i'
    # if ends in _ o
    if 'o' in guess and 'o' in wrd:
        if wrd[len(wrd)-2] == 'o':
            while y != 0:
                ltr = amod[randint(0,484604)-1]
                if ltr not in guess:
                    y = 0
    # if ends in _ i
    if 'i' in guess and 'i' in wrd:
        if wrd[len(wrd)-2] == 'i':
            while y != 0:
                ltr = amod[randint(0,484604)-1]
                if ltr not in guess:
                    y = 0
    # if ends in _ u
    if 'u' in guess and 'u' in wrd:
        if wrd[len(wrd)-2] == 'u':
            if 'a' not in guess:
                ltr = 'a'
    # if ends in _ q
    if 'q' in guess and 'q' in wrd:
        if wrd[len(wrd)-2] == 'q':
            if 'a' not in guess:
                ltr = 'a'
    # if ends in _ w
    if 'w' in guess and 'w' in wrd:
        if wrd[len(wrd)-2] == 'w':
            if 'o' not in guess:
                ltr = 'o'
            elif 'a' not in guess:
                ltr = 'a'
            elif 'e' not in guess:
                ltr = 'e'
    # if ends in _ r
    if 'r' in guess and 'r' in wrd:
        if wrd[len(wrd)-2] == 'r':
            if 'e' not in guess:
                ltr = 'e'   
    # if ends in _ t
    if 't' in guess and 't' in wrd:
        if wrd[len(wrd)-2] == 't':
            if 's' not in guess:
                ltr = 's'
            elif 'n' not in guess:
                ltr = 'n'
    # if ends in _ y
    if 'y' in guess and 'y' in wrd:
        if wrd[len(wrd)-2] == 'y':
            opt = ['a', 'm', 'n', 'o', 'p', 'r', 'x']
            if 'l' not in guess:
                ltr = 'l'
            elif 't' not in guess:
                ltr = 't'
            elif 'r' not in guess:
                ltr = 'r'
    # if ends in _ p
    if 'p' in guess and 'p' in wrd:
        if wrd[len(wrd)-2] == 'p':
            if 'i' not in guess:
                ltr = 'i'
            elif 'o' not in guess:
                ltr = 'o'
    # if ends in _ s
    if 's' in guess and 's' in wrd:
        if wrd[len(wrd)-2] == 's':
            if 'e' not in guess:
                ltr = 'e'
            elif 'r' not in guess:
                ltr = 'r'
            elif 't' not in guess:
                ltr = 't'
    # if ends in _ d
    if 'd' in guess and 'd' in wrd:
        if wrd[len(wrd)-2] == 'd':
            if 'e' not in guess:
                ltr = 'e'
    # if ends in _ f
    if 'f' in guess and 'f' in wrd:
        if wrd[len(wrd)-2] == 'f':
            if 'o' not in guess:
                ltr = 'o'
            elif 'l' not in guess:
                ltr = 'l'
    # if ends in _ g
    if 'g' in guess and 'g' in wrd:
        if wrd[len(wrd)-2] == 'g':
            if 'n' not in guess:
                ltr = 'n'
    # if ends in _ h
    if 'h' in guess and 'h' in wrd:
        if wrd[len(wrd)-2]  == 'h':
            if 's' not in guess:
                ltr = 's'
            elif 'c' not in guess:
                ltr = 'c'
            elif 't' not in guess:
                ltr = 't'
    # if ends in _ j
    if 'j' in guess and 'j' in wrd:
        if wrd[len(wrd)-2] == 'j':
            if 'a' not in guess:
                ltr = 'a'
    # if ends in _ k
    if 'k' in guess and 'k' in wrd:
        if wrd[len(wrd)-2] == 'k':
            if 'c' not in guess:
                ltr = 'c'
            elif 'r' not in guess:
                ltr = 'r'
    # if ends in _ l
    if 'l' in guess and 'l' in wrd:
        if wrd[len(wrd)-2] == 'l':
            if 'a' not in guess:
                ltr = 'a'
    # if ends in _ z 
    if 'z' in guess and 'z' in wrd:
        if wrd[len(wrd)-2] == 'z':
            if 't' not in guess:
                ltr = 't'
    # if ends in _ x
    if 'x' in guess and 'x' in wrd:
        if wrd[len(wrd)-2] == 'x':
            if 'o' not in guess:
                ltr = 'o'
            elif 'e' not in guess:
                ltr = 'e'
            elif 'a' not in guess:
                ltr = 'a'
    # if ends in _ c
    if 'c' in guess and 'c' in wrd:
        if wrd[len(wrd)-2] == 'c':
            if 'i' not in guess:
                ltr = 'i'
    # if ends in _ v
    if 'v' in guess and 'v' in wrd:
        if wrd[len(wrd)-2] == 'v':
            if 'e' not in guess:
                ltr = 'e'
            elif 'o' not in guess:
                ltr = 'o'
            elif 'i' not in guess:
                ltr = 'i'
            elif 'a' not in guess:
                ltr = 'a'
    # if ends in _ b
    if 'b' in guess and 'b' in wrd:
        if wrd[len(wrd)-2] == 'b':
            if 'm' not in guess:
                ltr = 'm'
            elif 'a' not in guess:
                ltr = 'a'
    # if ends in _ n
    if 'n' in guess and 'n' in wrd:
        if wrd[len(wrd)-2] == 'n':
            if 'o' not in guess:
                ltr = 'o'
            elif 'e' not in guess:
                ltr = 'e'
            elif 'a' not in guess:
                ltr = 'a'
    # if ends in _ m
    if 'm' in guess and 'm' in wrd:
        if wrd[len(wrd)-2] == 'm':
            if 's' not in guess:
                ltr = 's'
            elif 'u' not in guess:
                ltr = 'u'
    return ltr

    
def sfx2(guess, wrd): #Guessing when second to last letter is revealed
    ltr = ''
    r = 1
    # if ends in e _
    if 'e' in guess and 'e' in wrd:
        if wrd[len(wrd)-3] == 'e':
            if 's' not in guess:
                ltr = 's'
            elif 'd' not in guess:
                ltr = 'd'
            elif 'r' not in guess:
                ltr = 'r'
            elif 'n' not in guess:
                ltr = 'n'
    # if ends in a _ 
    if 'a' in guess and 'a' in wrd:
        if wrd[len(wrd)-3] == 'a':
            if 'l' not in guess:
                ltr = 'l'
            elif 'n' not in guess:
                ltr = 'n'
            elif 'r' not in guess:
                ltr = 'r'
    # if ends in o _
    if 'o' in guess and 'o' in wrd:
        if wrd[len(wrd)-3] == 'o':
            if 'n' not in guess:
                ltr = 'n'
            elif 'r' not in guess:
                ltr = 'r'
            elif 't' not in guess:
                ltr = 't'
    # if ends in i _ 
    if 'i' in guess and 'i' in wrd:
        if wrd[len(wrd)-3] == 'i':
            if 'c' not in guess:
                ltr = 'c'
            elif 'n' not in guess:
                ltr = 'n'
            elif 's' not in guess:
                ltr = 's'
    # if ends in u _
    if 'u' in guess and 'u' in wrd:
        if wrd[len(wrd)-3] == 'u':
            if 's' not in guess:
                ltr = 's'
            elif 'm' not in guess:
                ltr = 'm'
            elif 'l' not in guess:
                ltr = 'l'
    # if ends in q _
    if 'q' in guess and 'q' in wrd:
        if wrd[len(wrd)-3] == 'q':
            pass
    # if ends in w _
    if 'w' in guess and 'w' in wrd:
        if wrd[len(wrd)-3] == 'w':
            if 'y' not in guess:
                ltr = 'y'
            elif 't' not in guess:
                ltr = 't'
            elif 'e' not in guess:
                ltr = 'e'
            elif 'i' not in guess:
                ltr = 'i'
    # if ends in r _
    if 'r' in guess and 'r' in wrd:
        if wrd[len(wrd)-3] == 'r':
            if 's' not in guess:
                ltr = 's'
            elif 'y' not in guess:
                ltr = 'y'
            elif 'e' not in guess:
                ltr = 'e'   
    # if ends in t _
    if 't' in guess and 't' in wrd:
        if wrd[len(wrd)-3] == 't':
            if 's' not in guess:
                ltr = 's'
            elif 'e' not in guess:
                ltr = 'e'
            elif 'y' not in guess:
                ltr = 'y'
    # if ends in y _
    if 'y' in guess and 'y' in wrd:
        if wrd[len(wrd)-3] == 'y':
            opt = ['a', 'm', 'n', 'o', 'p', 'r', 'x']
            if 's' not in guess:
                ltr = 's'
            elif 'l' not in guess:
                ltr = 'l'
            elif 'e' not in guess:
                ltr = 'e'
    # if ends in p _
    if 'p' in guess and 'p' in wrd:
        if wrd[len(wrd)-3] == 'p':
            if 's' not in guess:
                ltr = 's'
            elif 'e' not in guess:
                ltr = 'e'
            elif 'y' not in guess:
                ltr = 'y'
    # if ends in s _
    if 's' in guess and 's' in wrd:
        if wrd[len(wrd)-3] == 's':
            if 't' not in guess:
                ltr = 't'
            elif 'e' not in guess:
                ltr = 'e'
            elif 'm' not in guess:
                ltr = 'm'
            elif 'h' not in guess:
                ltr = 'h'
    # if ends in d _
    if 'd' in guess and 'd' in wrd:
        if wrd[len(wrd)-3] == 'd':
            if 's' not in guess:
                ltr = 's'
            elif 'e' not in guess:
                ltr = 'e'
            elif 'y' not in guess:
                ltr = 'y'
    # if ends in f _
    if 'f' in guess and 'f' in wrd:
        if wrd[len(wrd)-3] == 'f':
            if 'y' not in guess:
                ltr = 'y'
            elif 's' not in guess:
                ltr = 's'
            elif 't' not in guess:
                ltr = 't'
    # if ends in g _
    if 'g' in guess and 'g' in wrd:
        if wrd[len(wrd)-3] == 'g':
            if 's' not in guess:
                ltr = 's'
            elif 'e' not in guess:
                ltr = 'e'
            elif 'y' not in guess:
                ltr = 'y'
    # if ends in h _
    if 'h' in guess and 'h' in wrd:
        if wrd[len(wrd)-3]  == 'h':
            if 's' not in guess:
                ltr = 's'
            elif 'y' not in guess:
                ltr = 'y'
            elif 't' not in guess:
                ltr = 't'
    # if ends in j _
    if 'j' in guess and 'j' in wrd:
        if wrd[len(wrd)-3] == 'j':
            if 'o' not in guess:
                ltr = 'o'
            else:
                ltr = 'i'
    # if ends in k _
    if 'k' in guess and 'k' in wrd:
        if wrd[len(wrd)-3] == 'k':
            if 's' not in guess:
                ltr = 's'
            elif 'e' not in guess:
                ltr = 'e'
            elif 'y' not in guess:
                ltr = 'y'
    # if ends in l _
    if 'l' in guess and 'l' in wrd:
        if wrd[len(wrd)-3] == 'l':
            if 'y' not in guess:
                ltr = 'y'
            elif 'e' not in guess:
                ltr = 'e'
            elif 's' not in guess:
                ltr = 's'
    # if ends in z _ 
    if 'z' in guess and 'z' in wrd:
        if wrd[len(wrd)-3] == 'z':
            if 'e' not in guess:
                ltr = 'e'
            elif 'y' not in guess:
                ltr = 'y'
            elif 'i' not in guess:
                ltr = 'i'
            elif 'o' not in guess:
                ltr = 'o'
    # if ends in x _
    if 'x' in guess and 'x' in wrd:
        if wrd[len(wrd)-3] == 'x':
            if 'y' not in guess:
                ltr = 'y'
            elif 't' not in guess:
                ltr = 't'
            elif 'e' not in guess:
                ltr = 'e'
            elif 'i' not in guess:
                ltr = 'i'
    # if ends in c _
    if 'c' in guess and 'c' in wrd:
        if wrd[len(wrd)-3] == 'c':
            if 'e' not in guess:
                ltr = 'e'
            elif 'k' not in guess:
                ltr = 'k'
            elif 'h' not in guess:
                ltr = 'h'
    # if ends in v _
    if 'v' in guess and 'v' in wrd:
        if wrd[len(wrd)-3] == 'v':
            if 'e' not in guess:
                ltr = 'e'
    # if ends in b _
    if 'b' in guess and 'b' in wrd:
        if wrd[len(wrd)-3] == 'b':
            if 's' not in guess:
                ltr = 's'
            elif 'e' not in guess:
                ltr = 'e'
            elif 'y' not in guess:
                ltr = 'y'
    # if ends in n _
    if 'n' in guess and 'n' in wrd:
        if wrd[len(wrd)-3] == 'n':
            if 'g' not in guess:
                ltr = 'g'
            elif 's' not in guess:
                ltr = 's'
            elif 't' not in guess:
                ltr = 't'
            elif 'e' not in guess:
                ltr = 'e'
    # if ends in m _
    if 'm' in guess and 'm' in wrd:
        if wrd[len(wrd)-3] == 'm':
            if 's' not in guess:
                ltr = 's'
            elif 'e' not in guess:
                ltr = 'e'
    return ltr

def hng(x, wrd,w): #keeps track of the print statements for the guessing portion of the game, w defines who is guessing, x is the number of strikes
    if x == 0:
        pic = Base
    elif x == 1:
        pic = Strk_1
    elif x == 2:
        pic = Strk_2
    elif x == 3:
        pic = Strk_3
    elif x == 4:
        pic = Strk_4
    elif x == 5:
        pic = Strk_5
    elif x == 6:
        pic = Strk_6
        if w == 0:
            print('Too many incorrect guesses, Game over.')
            print('The correct word was %s' % wrd + '\n')
            statr['losses'] += 1
        else:
            print("The Computer gets 3 extra guesses.")
    for i in pic:
        print(i)
    print('')
    print('')


Base = ['        xxxxxxxx    ',
        '        x      x    ',
        '               x    ',
        '               x    ',
        '               x    ',
        '               x    ',
        '               x    ',
        '               x    ',
        '               x    ',
        '               x    ',
        '               x    ',
        '               x    ',
        '         xxxxxxxxxxx']
        
Strk_1 = ['        xxxxxxxx    ',
          '        x      x    ',
          '      *****    x    ',
          '      *   *    x    ',
          '      *****    x    ',
          '               x    ',
          '               x    ',
          '               x    ',
          '               x    ',
          '               x    ',
          '               x    ',
          '               x    ',
          '         xxxxxxxxxxx']

Strk_2 = ['        xxxxxxxx    ',
          '        x      x    ',
          '      *****    x    ',
          '      *   *    x    ',
          '      *****    x    ',
          '        *      x    ',
          '        *      x    ',
          '        *      x    ',
          '        *      x    ',
          '               x    ',
          '               x    ',
          '               x    ',
          '         xxxxxxxxxxx']

Strk_3 = ['        xxxxxxxx    ',
          '        x      x    ',
          '      *****    x    ',
          '      *   *    x    ',
          '      *****    x    ',
          '        *   *  x    ',
          '        * *    x    ',
          '        *      x    ',
          '        *      x    ',
          '               x    ',
          '               x    ',
          '               x    ',
          '         xxxxxxxxxxx']

Strk_4 = ['        xxxxxxxx    ',
          '        x      x    ',
          '      *****    x    ',
          '      *   *    x    ',
          '      *****    x    ',
          '    *   *   *  x    ',
          '      * * *    x    ',
          '        *      x    ',
          '        *      x    ',
          '               x    ',
          '               x    ',
          '               x    ',
          '         xxxxxxxxxxx']

Strk_5 = ['        xxxxxxxx    ',
          '        x      x    ',
          '      *****    x    ',
          '      *   *    x    ',
          '      *****    x    ',
          '    *   *   *  x    ',
          '      * * *    x    ',
          '        *      x    ',
          '        *      x    ',
          '      *        x    ',
          '    *          x    ',
          '               x    ',
          '         xxxxxxxxxxx']
        
Strk_6 = ['        xxxxxxxx    ',
          '        x      x    ',
          '      *****    x    ',
          '      *   *    x    ',
          '      *****    x    ',
          '    *   *   *  x    ',
          '      * * *    x    ',
          '        *      x    ',
          '        *      x    ',
          '      *   *    x    ',
          '    *       *  x    ',
          '               x    ',
          '         xxxxxxxxxxx']
 

def again(w): #Asks the user if they want to play again
    z = 1
    wnt = input('Do you wish to play again? y/n ').lower()
    if wnt == 'y':
        while z!=0:
            nxt = input('Do you wish to guess(1) or let the Computer guess(2)? ')
            if nxt == '1':
                r()
            elif nxt == '2':
                q()
            else:
                q_cull()
    else:
        if statq['losses']+statq['wins'] !=0:
            statq['Win Percentage'] = (statq['wins']/ (statq['losses']+statq['wins']))*100
        if statr['losses']+statr['wins'] !=0:
            statr['Win Percentage'] = (statr['wins']/ (statr['losses']+statr['wins']))*100
        print('Thank you for playing')
        sleep(.5)
        print('Final Statistics')
        sleep(.5)
        print('User Guessing: %s, Computer Guessing: %s' % (statr, statq))
        sleep(.5)
        sleep (7.5)
        exit()



def r(): #Runs the game if user is guessing
    xl = randint(0,58110)
    wrd = lex[xl]
    hng(0, wrd,0)
    shw = ''
    guess = []
    strk = 0
    win = False
    wrng = []
    cls = 0
    sld = False
    fnl = 0
    #print(wrd)
    print('_ ' *(len(wrd)-1))
    while strk < 6 and win != True:
        wrng = []
        fnl = 0
        cls = 0
        shw = ''
        hj = 0
        while hj != True:
            ltr = input('Guess a letter or solve the word: ').lower()
            if ltr in alphabet and ltr not in guess:
                hj = True
            elif ltr + '\n' in lex:
                hj = True
                fnl = True
        if fnl == True:
            if wrd[0:len(wrd)-1] == ltr:
                win = True
                sleep(.5)
                print('Congratulations! You won!'+'\n')
                continue
        guess.append(ltr)
        sleep(.5)
        if ltr not in wrd:
            sld = True
            print('Sorry, Incorrect')
            strk+=1
        else:
            print('Correct!')
        for x in guess:
            if x not in wrd:
                wrng.append(x)
        for i in wrd:
            if i in guess:
                shw+= i+' '
                cls += 1
            else:
                if wrd.index(i) != len(wrd)-1:
                    shw+= '_ '
        print('')
        sleep(.5)
        print(shw)
        print('Wrong Guesses: %s' % wrng)
        if cls == len(wrd)-1:
            win = True
            print('Congratulations! You won!')
            statr['wins'] +=1
        if sld == True:
            hng(strk, wrd,0)
    again(1)



def cull(crct,wrng,wrd,exl): #For the optimized game, crct is list of correct guesses, wrng is list of incorrect guesses, wrd is the target word, exl is the copy of the lex list of words 
    weight = {}
    for i in alphabet:
        weight[i] = 0
    opt = []
    non = []
    x = 0
    for e in exl:
        if len(exl)==x:
            break
        fl = 0
        lf = 0
        if e == 'ruthless':
            print(e)
        elif e == 'undefined':
            print(e)
        elif e == 'haiku':
            print(e)
        elif e == 'elusive':
            print(e)
        elif e == 'baboon':
            print(e)
        for s in wrng:
            if s in e and fl == 0 : #For all of the incorrect guesses, if the guessed letter is in the word, remove the word from the list of words
                non.append(e)
                fl = 1
                continue
        if fl == 1:
            continue #If the word has already been removed from the list, skip the rest of the loop
        if len(e) != len(wrd):
            non.append(e)
            continue
        for c in crct:
            n = crct[c]
            if n == 'null':
                continue
            if n!=e[c] and lf==0:
                non.append(e)
                lf = 1
                continue
        if lf == 1:
            continue
        e = e[0:len(e)-1] #Chop off the newline attached to the word
        for t in e: #For all of the letters that make up the word, add an instance to it in the dictionary
            weight[t]+=1
    for z in weight:
        if z in wrd:
            if crct[wrd.index(z)] != 'null':
                continue
        sub = 0
        while sub < weight[z]:
            opt.append(z) #Creates the weighted list
            sub+=1
    for n in non:
        exl.remove(n)
    ret = [opt, exl]
    #print(opt)
    #print(exl)
    return ret


def q_cull(): #Attempt at an optimized code for when the computer is guessing, so that the computer will almost always get the word
    exl = lex[0:len(lex)]
    with open('second.txt', 'r+') as file:
        file.truncate(0)
    ky = 0
    wrd = ''
    hng(0, wrd,1)
    shw = ''
    guess = []
    strk = 0
    crct = {}
    sld = False
    win = False
    wrng = []
    ltr = ''
    cls = 0
    n = 2
    sld = False
    ltr2 = ''
    while ky!=1: #Until the word is a valid choice
        wrd = input('What is your chosen word? ').lower()
        wrd += '\n'
        if wrd in lex:
            ky = 1
            print('_ ' *(len(wrd)-1))
        else:
            print('That is not a valid word.')
    for f in range(0,len(wrd)-1):
        crct[f] = 'null'
    while win != True and strk < 9:
        shw = ''
        myb = []
        cls = 0
        if len(guess) == 0 : #If no letter has been correctly guessed yet
            ltr = amod[randint(0,484604)-1] #Letter guessed is based off of the original weighted list
        else:
            ret = cull(crct,wrng,wrd,exl) #Call the cull function to access a new weighted list
            opt = ret[0]
            exl= ret[1]
            ltr = opt[randint(0,len(opt)-1)] #Random letter based on the weighted chances of each possible letter
        #print('10: %s' % ltr)
        guess.append(ltr)
        sleep(1)
        print('The Computer guesses letter %s.' % ltr)
        sleep(1)
        if ltr not in wrd:
            sld = True
            print('The Computer guessed wrongly!')
            strk+=1
            wrng.append(ltr)
        else:
            n = 2
            print('The Computer is correct.')
            with open('second.txt', 'r+') as file:
                file.truncate(0)
            with open('second.txt', 'w') as file:
                file.write(ltr)
        for i in range(1, len(wrd)):
            if wrd[i-1] in guess:
                shw += wrd[i-1]+ ' '
                cls += 1
                crct[i-1] = wrd[i-1]
            else:
                shw+= '_ '
        print('')
        sleep(.5)
        print(shw)
        print('Wrong Computer Guesses: %s' % wrng)
        if cls == len(wrd)-1:
            win = True
            print('Sorry, the Computer won this round.')
            statq['losses'] += 1
        if sld == True:
            if strk == 9:
                print("The Computer has guessed incorrectly too many times. you've won!")
                statq['wins'] += 1
            if strk <= 6:
                hng(strk, wrd,1)
    again(2)
        
def q_cullrs(): #Statistical version of q_cull function
    exl = lex[0:len(lex)]
    with open('second.txt', 'r+') as file:
        file.truncate(0)
    ky = 0
    wrd = ''
    shw = ''
    guess = []
    strk = 0
    crct = {}
    sld = False
    win = False
    wrng = []
    ltr = ''
    cls = 0
    n = 2
    sld = False
    ltr2 = ''
    while ky!=1: #Until the word is a valid choice
        #wrd = input('What is your chosen word? ').lower()
        #wrd += '\n'
        xl = randint(0,len(lex))
        wrd = lex[xl]
        if wrd in lex:
            ky = 1
        else:
            pass
    for f in range(0,len(wrd)-1):
        crct[f] = 'null'
    while win != True and strk < 9:
        shw = ''
        myb = []
        cls = 0
        if len(guess) == 0 : #If no letter has been correctly guessed yet
            ltr = amod[randint(0,484604)-1] #Letter guessed is based off of the original weighted list
        else:
            ret = cull(crct,wrng,wrd,exl) #Call the cull function to access a new weighted list
            opt = ret[0]
            exl= ret[1]
            ltr = opt[randint(0,len(opt)-1)] #Random letter based on the weighted chances of each possible letter
        guess.append(ltr)
        if ltr not in wrd:
            sld = True
            strk+=1
            wrng.append(ltr)
        else:
            n = 2

            with open('second.txt', 'r+') as file:
                file.truncate(0)
            with open('second.txt', 'w') as file:
                file.write(ltr)
        for i in range(1, len(wrd)):
            if wrd[i-1] in guess:
                shw += wrd[i-1]+ ' '
                cls += 1
                crct[i-1] = wrd[i-1]
            else:
                shw+= '_ '
        if cls == len(wrd)-1:
            win = True
            statq['losses'] += 1
        if sld == True:
            if strk == 9:
                statq['wins'] += 1
                print(wrd)
            if strk <= 6:
                pass


def q(): #Original code for when the computer is guessing, around 60% accuracy 
    y = 1
    with open('second.txt', 'r+') as file:
        file.truncate(0)
    ky = 0
    wrd = ''
    hng(0, wrd,1)
    shw = ''
    guess = []
    strk = 0
    crct = {}
    win = False
    wrng = []
    ltr = ''
    ct = []
    cls = 0
    sld = False
    fnl = 0
    n = 2
    uk = 0
    fj = False
    lv = False
    bef = ''
    aft = ''
    num = []
    while ky!=1:
        wrd = input('What is your chosen word? ').lower()
        wrd += '\n'
        if wrd in lex:
            ky = 1
            print('_ ' *(len(wrd)-1))
        else:
            print('That is not a valid word.')
    for f in range(0,len(wrd)-1):
        crct[f] = 'null'
    while win != True and strk < 9:
        myb = []
        ku = []
        p = 1
        ltr2 = ''
        num = []
        fj = False
        xz = 1
        bef = ''
        aft = ''
        ltr = ''
        aft2 = ''
        wrng = []
        shw = ''
        y = 1
        cz = 1
        vwl = 0
        sc = 1
        #print('1: %s' % ltr)
        #Don't guess vowels if too prevalent
        for i in wrd:
            if i in vwls and i in guess:
                vwl += 1
        if vwl > (len(wrd) -1)/2:
            lv = True
        #print('2: %s' % ltr)
        # Guess 2nd of word pair
        with open('second.txt', 'r') as file:
            ltr = file.readline()
        if ltr in alphabet and ltr not in guess:
            y = 0
            p = 0
            xz = 0
            cls = 1
            cz = 0
            sc = 0
        #print('3: %s' % ltr)
        # Guess Vowels First
        if cls == 0:
            if strk == 5:
                ltr = 'y'
                p = 0
                y = 0
                xz = 0
                sc = 0
                cz = 0
            while p != 0:
                ltr = vwls[randint(0,len(vwls)-1)]
                if ltr not in guess:
                    p = 0
                    y = 0
                    xz = 0
                    cz = 0
                    sc = 0
                if lv == True:
                    if ltr in vwls:
                        p = 1
                        y = 1
                        xz = 1
                        cz = 1
                        sc = 1
        #print('4: %s' % ltr)
        # Complete the word w/ one letter left
        if cls == len(wrd)-2 and cz != 0:
            for c in crct:
                if crct[c] == 'null':
                    uk = c
            for i in range(0,len(wrd)-1):
                num.append(i)
            num.pop(uk)
            for x in num:
                if x < uk:
                    bef+=wrd[x]
                elif x > uk:
                    aft += wrd[x]
            for z in alphabet:
                tp = '%s%s%s\n' % (bef, z, aft)
                if tp in lex and z not in guess:
                    myb.append(z)
                    y = 0
            if len(myb) > 0:
                d = myb[randint(0,len(myb)-1)]
                ltr = d
            y = 0
            xz = 0
            sc = 0
        #print('5: %s' % ltr)
        # If ends in i _ _
        if 'i' in guess and 'i' in wrd and sc != 0:
            if wrd[len(wrd)-4] == 'i' and wrd[len(wrd)-3] not in guess and wrd[len(wrd)-2] not in guess:
                if 'n' not in guess:
                    ltr = 'n'
                    y = 0
                    xz = 0
            elif 'n' in guess and wrd[len(wrd)-3] == 'n' and wrd[len(wrd)-2] not in guess:
                if 'g' not in guess:
                    ltr = 'g'
                    y = 0
                    xz = 0
            elif 'n' in guess and wrd[len(wrd)-2] == 'n' and wrd[len(wrd)-3] not in guess:
                if 'o' not in guess:
                    ltr = 'o'
                    y = 0
                    xz = 0
        # If q in word
        if 'q' in wrd and 'q' in guess:
            ltr = 'u'
            y = 0
            xz = 0
        #print('6: %s' % ltr)
        # Complete the word w/ two letters left
        if cls == len(wrd)-3:
            for c in crct:
                if crct[c] == 'null':
                    #uk = c
                    ku.append(c)
            for i in range(0,len(wrd)):
                num.append(i)
            num.pop(ku[0])
            num.pop(ku[1]-1)
            for x in num:
                if x < ku[0]:
                    bef+=wrd[x]
                elif x > ku[0] and x < ku[1]:
                    aft += wrd[x]
                elif x > ku[1]:
                    aft2+= wrd[x]
            for z in alphabet:
                for g in alphabet:
                    tp = '%s%s%s%s%s' % (bef, z, aft, g, aft2)
                    if tp in lex and z not in guess and g not in guess:
                        myb.append(z)
                        ltr2 = g
                        y = 0
            if len(myb) > 0:
                d = myb[randint(0,len(myb)-1)]
                ltr = d
                y = 0
                xz = 0
        cls = 0
        #print('7: %s' % ltr)
        # 2 Letter Combinations
        if wrd[1] in guess and xz != 0 and wrd[0] not in guess:
            ltr = pfx2(guess, wrd)
            if ltr in alphabet:
                y = 0
                xz = 0
        if wrd[len(wrd)-2] in guess and xz != 0 and wrd[len(wrd)-3] not in guess:
            ltr = sfx(guess,wrd)
            if ltr in alphabet:
                y = 0
                xz = 0
        if wrd[0] in guess and xz != 0 and wrd[1] not in guess:
            ltr = pfx(guess, wrd)
            if ltr in alphabet:
                y = 0
                xz = 0
        if wrd[len(wrd)-3] in guess and xz != 0 and wrd[len(wrd)-2] not in guess:
            ltr = sfx2(guess, wrd)
            if ltr in alphabet:
                y = 0
        #print('8: %s' % ltr)
        # 3 Letter Combinations
        if y != 0 and n != 0:
            ltr = thr(guess, wrd)
            if ltr in alphabet:
                y = 0
                if ltr not in wrd:
                    n -= 1
        #print('9: %s' % ltr)
        # If All Else Fails
        while y != 0:
            ltr = amod[randint(0,484604)-1]
            #ltr = input('Ltr: ').lower()
            if ltr not in guess:
                y = 0
            if lv == True and ltr in vwls:
                y = 1
        #print('10: %s' % ltr)
        guess.append(ltr)
        sleep(1)
        print('The Computer guesses letter %s.' % ltr)
        sleep(1)
        if ltr not in wrd:
            sld = True
            print('The Computer guessed wrongly!')
            strk+=1
        else:
            n = 2
            print('The Computer is correct.')
            with open('second.txt', 'r+') as file:
                file.truncate(0)
            with open('second.txt', 'w') as file:
                file.write(ltr2)
        for x in guess:
            if x not in wrd:
                wrng.append(x)
        for i in range(1, len(wrd)):
            if wrd[i-1] in guess:
                shw += wrd[i-1]+ ' '
                cls += 1
                crct[i-1] = wrd[i-1]
            else:
                shw+= '_ '
        print('')
        sleep(.5)
        print(shw)
        print('Wrong Computer Guesses: %s' % wrng)
        if cls == len(wrd)-1:
            win = True
            print('Sorry, the Computer won this round.')
            statq['losses'] += 1
        if sld == True:
            if strk == 9:
                print("The Computer has guessed incorrectly too many times. you've won!")
                statq['wins'] += 1
            if strk <= 6:
                hng(strk, wrd,1)
    again(2)

e_blank = {}
a_blank = {}
b_blank = {}
c_blank = {}
d_blank = {}
f_blank = {}
g_blank = {}
h_blank = {}
i_blank = {}
j_blank = {}
k_blank = {}
l_blank = {}
m_blank = {}
n_blank = {}
o_blank = {}
p_blank = {}
q_blank = {}
r_blank = {}
s_blank = {}
t_blank = {}
u_blank = {}
v_blank = {}
w_blank = {}
x_blank = {}
y_blank = {}
z_blank = {}


for i in alphabet: #Generates three a dictionary with keys as three letter combinations
    for v in alphabet:
            e_blank['e'+ i + v] = 0
            a_blank['a'+ i + v] = 0
            b_blank['b'+ i + v] = 0
            c_blank['c'+ i + v] = 0
            d_blank['d'+ i + v] = 0
            f_blank['f'+ i + v] = 0
            g_blank['g'+ i + v] = 0
            h_blank['h'+ i + v] = 0
            i_blank['i'+ i + v] = 0
            j_blank['j'+ i + v] = 0
            k_blank['k'+ i + v] = 0
            l_blank['l'+ i + v] = 0
            m_blank['m'+ i + v] = 0
            n_blank['n'+ i + v] = 0
            o_blank['o'+ i + v] = 0
            p_blank['p'+ i + v] = 0
            q_blank['q'+ i + v] = 0
            r_blank['r'+ i + v] = 0
            s_blank['s'+ i + v] = 0
            t_blank['t'+ i + v] = 0
            u_blank['u'+ i + v] = 0
            v_blank['v'+ i + v] = 0
            w_blank['w'+ i + v] = 0
            x_blank['x'+ i + v] = 0
            y_blank['y'+ i + v] = 0
            z_blank['z'+ i + v] = 0

def s(): #Finds the instances of each three letter combination for probabilities(original code)
    hj = 0
    alpha = {}
    for i in alphabet:
        alpha[i] = 0
    lim = 3
    for xl in lex:
        sub = 0
        for vx in xl:
            if vx == 'e' and sub <= len(xl)-4:
                 e_blank['e'+ xl[sub+1] + xl[sub+2]] += 1
            if vx == 'a' and sub <= len(xl)-4:
                 a_blank['a'+ xl[sub+1] + xl[sub+2]] += 1
            if vx == 'b' and sub <= len(xl)-4:
                 b_blank['b'+ xl[sub+1] + xl[sub+2]] += 1
            if vx == 'c' and sub <= len(xl)-4:
                 c_blank['c'+ xl[sub+1] + xl[sub+2]] += 1
            if vx == 'd' and sub <= len(xl)-4:
                 d_blank['d'+ xl[sub+1] + xl[sub+2]] += 1
            if vx == 'f' and sub <= len(xl)-4:
                 f_blank['f'+ xl[sub+1] + xl[sub+2]] += 1
            if vx == 'g' and sub <= len(xl)-4:
                 g_blank['g'+ xl[sub+1] + xl[sub+2]] += 1
            if vx == 'h' and sub <= len(xl)-4:
                 h_blank['h'+ xl[sub+1] + xl[sub+2]] += 1
            if vx == 'i' and sub <= len(xl)-4:
                 i_blank['i'+ xl[sub+1] + xl[sub+2]] += 1
            if vx == 'j' and sub <= len(xl)-4:
                 j_blank['j'+ xl[sub+1] + xl[sub+2]] += 1
            if vx == 'k' and sub <= len(xl)-4:
                 k_blank['k'+ xl[sub+1] + xl[sub+2]] += 1
            if vx == 'l' and sub <= len(xl)-4:
                 l_blank['l'+ xl[sub+1] + xl[sub+2]] += 1
            if vx == 'm' and sub <= len(xl)-4:
                 m_blank['m'+ xl[sub+1] + xl[sub+2]] += 1
            if vx == 'n' and sub <= len(xl)-4:
                 n_blank['n'+ xl[sub+1] + xl[sub+2]] += 1
            if vx == 'o' and sub <= len(xl)-4:
                 o_blank['o'+ xl[sub+1] + xl[sub+2]] += 1
            if vx == 'p' and sub <= len(xl)-4:
                 p_blank['p'+ xl[sub+1] + xl[sub+2]] += 1
            if vx == 'q' and sub <= len(xl)-4:
                 q_blank['q'+ xl[sub+1] + xl[sub+2]] += 1
            if vx == 'r' and sub <= len(xl)-4:
                 r_blank['r'+ xl[sub+1] + xl[sub+2]] += 1
            if vx == 's' and sub <= len(xl)-4:
                 s_blank['s'+ xl[sub+1] + xl[sub+2]] += 1
            if vx == 't' and sub <= len(xl)-4:
                 t_blank['t'+ xl[sub+1] + xl[sub+2]] += 1
            if vx == 'u' and sub <= len(xl)-4:
                 u_blank['u'+ xl[sub+1] + xl[sub+2]] += 1
            if vx == 'v' and sub <= len(xl)-4:
                 v_blank['v'+ xl[sub+1] + xl[sub+2]] += 1
            if vx == 'w' and sub <= len(xl)-4:
                 w_blank['w'+ xl[sub+1] + xl[sub+2]] += 1
            if vx == 'x' and sub <= len(xl)-4:
                 x_blank['x'+ xl[sub+1] + xl[sub+2]] += 1
            if vx == 'y' and sub <= len(xl)-4:
                 y_blank['y'+ xl[sub+1] + xl[sub+2]] += 1
            if vx == 'z' and sub <= len(xl)-4:
                 z_blank['z'+ xl[sub+1] + xl[sub+2]] += 1
            sub+=1



#Dictionaries to split up the three letter combos into four groups based on the number of instances(500,1000,1500,2000)
thrlet500 = {}
thrlet1000 = {}
thrlet1500 = {}
thrlet2000 = {}

def conv(blank):
    sub=0
    for z in blank:
        if blank[z] >= 2000:
            thrlet2000[z] = blank[z]
        elif blank[z] >= 1500:
            thrlet1500[z] = blank[z]
        elif blank[z] >= 1000:
            thrlet1000[z] = blank[z]
        elif blank[z] >= 500:
            thrlet500[z] = blank[z]


conv(a_blank)
conv(b_blank)
conv(c_blank)
conv(d_blank)
conv(e_blank)
conv(f_blank)
conv(g_blank)
conv(h_blank)
conv(i_blank)
conv(j_blank)
conv(k_blank)
conv(l_blank)
conv(m_blank)
conv(n_blank)
conv(o_blank)
conv(p_blank)
conv(q_blank)
conv(r_blank)
conv(s_blank)
conv(t_blank)
conv(u_blank)
conv(v_blank)
conv(w_blank)
conv(x_blank)
conv(y_blank)
conv(z_blank)




def hydra(): #Runs all the code, with input values to decide which functions to call
    lex = []
    with open('lexicon.txt', 'r') as newFile:
        for i in range(58110):
            hj = newFile.readline()
            lex.append(hj)
    lex.remove('cross-bun\n')
    for c in lex:
        if 'a' not in c and 'e' not in c and 'i' not in c and 'o' not in c and 'y' not in c and 'u' not in c:
            lex.remove(c)
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m', 'n', 'o','p','q','r','s','t','u','v','w','x','y','z']
    prb = {'a': 36650, 'b': 9046, 'c': 19909, 'd': 19367, 'e': 56003, 'f': 6876, 'g': 14299, 'h': 10402, 'i': 42631, 'j': 807, 'k': 3943, 'l': 26399, 'm': 12944, 'n': 34477, 'o': 29053, 'p': 14119, 'q': 870, 'r': 35208, 's': 41429, 't': 33933, 'u': 16500, 'v': 5130, 'w': 4127, 'x': 1391, 'y': 8349, 'z': 715}
    amod = []
    for i in prb:
        sub = 0
        while sub <= prb[i]:
            amod.append(i)
            sub+=1
    vwls = []
    for c in amod:
        if c == 'a' or c== 'i' or c == 'e' or c == 'o' or c =='u':
            vwls.append(c)
    p = 1
    print('Welcome to Hangman. There are two game modes from which to choose from.')
    while 1 != 0:
        chc = input('Do you wish to guess(1) or let the Computer guess(2)? ')
        if chc == '1' or chc == '2' or chc == '3':
            break
    if chc == '1':
        r()
    elif chc == '2':
        q()
    else:
        q_cull()
        
    


statq = {'wins': 0, 'losses': 0} #For when the computer is guessing
statr = {'wins': 0, 'losses': 0} #For when the user is guessing


s()
#Creates one massive dictionary with every single three letter combo
delta = dict(**a_blank, **b_blank, **c_blank, **d_blank, **e_blank, **f_blank, **g_blank, **h_blank, **i_blank, **j_blank, **k_blank, **l_blank, **m_blank, **n_blank, **o_blank, **p_blank, **q_blank, **r_blank, **s_blank, **t_blank, **u_blank, **v_blank, **w_blank, **x_blank, **y_blank, **z_blank)


def qrs(): #Copy of q() function but with provisions for statistics, to determine the chances of the computer guessing a word
    y = 1
    with open('second.txt', 'r+') as file:
        file.truncate(0)
    ky = 0
    wrd = ''
    #hng(0, wrd,1)
    shw = ''
    guess = []
    strk = 0
    crct = {}
    win = False
    wrng = []
    ltr = ''
    ct = []
    cls = 0
    sld = False
    fnl = 0
    n = 2
    uk = 0
    fj = False
    lv = False
    bef = ''
    aft = ''
    num = []
    while ky!=1:
        xl = randint(0,len(lex))
        wrd = lex[xl]
        if wrd in lex:
            ky = 1
        else:
            pass
    for f in range(0,len(wrd)-1):
        crct[f] = 'null'
    while win != True and strk < 9:
        myb = []
        ku = []
        p = 1
        ltr2 = ''
        num = []
        fj = False
        xz = 1
        bef = ''
        aft = ''
        ltr = ''
        aft2 = ''
        wrng = []
        shw = ''
        y = 1
        cz = 1
        vwl = 0
        sc = 1
        for i in wrd:
            if i in vwls and i in guess:
                vwl += 1
        if vwl > (len(wrd) -1)/2:
            lv = True
        with open('second.txt', 'r') as file:
            ltr = file.readline()
        if ltr in alphabet and ltr not in guess:
            y = 0
            p = 0
            xz = 0
            cls = 1
            cz = 0
            sc = 0
        if cls == 0:
            if strk == 5:
                ltr = 'y'
                p = 0
                y = 0
                xz = 0
                sc = 0
                cz = 0
            while p != 0:
                ltr = vwls[randint(0,len(vwls)-1)]
                if ltr not in guess:
                    p = 0
                    y = 0
                    xz = 0
                    cz = 0
                    sc = 0
                if lv == True:
                    if ltr in vwls:
                        p = 1
                        y = 1
                        xz = 1
                        cz = 1
                        sc = 1
        if cls == len(wrd)-2 and cz != 0:
            for c in crct:
                if crct[c] == 'null':
                    uk = c
            for i in range(0,len(wrd)-1):
                num.append(i)
            num.pop(uk)
            for x in num:
                if x < uk:
                    bef+=wrd[x]
                elif x > uk:
                    aft += wrd[x]
            for z in alphabet:
                tp = '%s%s%s\n' % (bef, z, aft)
                if tp in lex and z not in guess:
                    myb.append(z)
                    y = 0
            if len(myb) > 0:
                d = myb[randint(0,len(myb)-1)]
                ltr = d
            y = 0
            xz = 0
            sc = 0
        if 'i' in guess and 'i' in wrd and sc != 0:
            if wrd[len(wrd)-4] == 'i' and wrd[len(wrd)-3] not in guess and wrd[len(wrd)-2] not in guess:
                if 'n' not in guess:
                    ltr = 'n'
                    y = 0
                    xz = 0
            elif 'n' in guess and wrd[len(wrd)-3] == 'n' and wrd[len(wrd)-2] not in guess:
                if 'g' not in guess:
                    ltr = 'g'
                    y = 0
                    xz = 0
            elif 'n' in guess and wrd[len(wrd)-2] == 'n' and wrd[len(wrd)-3] not in guess:
                if 'o' not in guess:
                    ltr = 'o'
                    y = 0
                    xz = 0
        if 'q' in wrd and 'q' in guess:
            if 'u' not in guess:
                ltr = 'u'
                y = 0
                xz = 0
        if cls == len(wrd)-3:
            for c in crct:
                if crct[c] == 'null':
                    ku.append(c)
            for i in range(0,len(wrd)):
                num.append(i)
            num.pop(ku[0])
            num.pop(ku[1])
            for x in num:
                if x < ku[0]:
                    bef+=wrd[x]
                elif x > ku[0] and x < ku[1]:
                    aft += wrd[x]
                elif x > ku[1]:
                    aft2+= wrd[x]
            for z in alphabet:
                for g in alphabet:
                    tp = '%s%s%s%s%s' % (bef, z, aft, g, aft2)
                    if tp in lex and z not in guess and g not in guess:
                        myb.append(z)
                        ltr2 = g
                        y = 0
            if len(myb) > 0:
                d = myb[randint(0,len(myb)-1)]
                ltr = d
                y = 0
                xz = 0
        cls = 0
        if wrd[1] in guess and xz != 0 and wrd[0] not in guess:
            ltr = pfx2(guess, wrd)
            if ltr in alphabet:
                y = 0
                xz = 0
        if wrd[len(wrd)-2] in guess and xz != 0 and wrd[len(wrd)-3] not in guess:
            ltr = sfx(guess,wrd)
            if ltr in alphabet:
                y = 0
                xz = 0
        if wrd[0] in guess and xz != 0 and wrd[1] not in guess:
            ltr = pfx(guess, wrd)
            if ltr in alphabet:
                y = 0
                xz = 0
        if wrd[len(wrd)-3] in guess and xz != 0 and wrd[len(wrd)-2] not in guess:
            ltr = sfx2(guess, wrd)
            if ltr in alphabet:
                y = 0
        if y != 0 and n != 0:
            ltr = thr(guess, wrd)
            if ltr in alphabet:
                y = 0
                if ltr not in wrd:
                    n -= 1
        while y != 0:
            ltr = amod[randint(0,484604)-1]
            if ltr not in guess:
                y = 0
            if lv == True and ltr in vwls:
                y = 1
        guess.append(ltr)
        if ltr not in wrd:
            sld = True
            strk+=1
        else:
            n = 2
            with open('second.txt', 'r+') as file:
                file.truncate(0)
            with open('second.txt', 'w') as file:
                file.write(ltr2)
        for x in guess:
            if x not in wrd:
                wrng.append(x)
        for i in range(1, len(wrd)):
            if wrd[i-1] in guess:
                shw += wrd[i-1]+ ' '
                cls += 1
                crct[i-1] = wrd[i-1]
            else:
                shw+= '_ '
        if cls == len(wrd)-1:
            win = True
            statq['losses'] += 1
        if sld == True:
            if strk == 9:
                statq['wins'] += 1
            if strk <= 6:
                pass
from random import randint


#Commented out unless needed for statistics purposes, runs the qrs function
from datetime import*
"""
print('its working')
date = datetime.now()
minutei = date.minute
secondi = date.second

for i in range(10):
    print(i)
    q_cullrs()

statq['Win Percentage'] = (statq['wins']/ (statq['losses']+statq['wins']))*100
print('Final Statistics(100)')
sleep(.5)
print('Computer Guessing: %s' % statq)
print('done')

date = datetime.now()
minutef = date.minute
secondf = date.second
print('%d minutes, %d seconds'% (minutef-minutei,secondf-secondi))

for i in range(10):
    print(i)
    q_cull()

statq['Win Percentage'] = (statq['wins']/ (statq['losses']+statq['wins']))*100
print('Final Statistics(100)')
sleep(.5)
print('Computer Guessing: %s' % statq)
print('done')


date = datetime.now()
minutei = date.minute
secondi = date.second
for i in range(125):
    print(i)
    q_cullrs()

statq['Win Percentage'] = (statq['wins']/ (statq['losses']+statq['wins']))*100
print('Final Statistics(500)')
sleep(.5)
print('Computer Guessing: %s' % statq)
date = datetime.now()
minutef = date.minute
secondf = date.second

for i in range(500):
    print(i)
    q_cull()

statq['Win Percentage'] = (statq['wins']/ (statq['losses']+statq['wins']))*100
print('Final Statistics(500)')
sleep(.5)
print('Computer Guessing: %s' % statq)


for i in range(1000):
    print(i)
    q_cull()

statq['Win Percentage'] = (statq['wins']/ (statq['losses']+statq['wins']))*100
print('Final Statistics(1000)')
sleep(.5)
print('Computer Guessing: %s' % statq)


for i in range(10000):
    print(i)
    q_cull()

statq['Win Percentage'] = (statq['wins']/ (statq['losses']+statq['wins']))*100
print('Final Statistics(10000)')
sleep(.5)
print('Computer Guessing: %s' % statq)

"""
