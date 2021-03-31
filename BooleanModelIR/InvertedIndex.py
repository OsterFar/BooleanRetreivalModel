import re
from .Preprocessing import unique
def tokenization_caseFoldingg() :
    noDoc = 50
    tokens = {}

    for i in range(noDoc) :
        myfile = open('AllFiles/{0}.txt'.format(i+1), encoding='utf-8')
        string  = myfile.read()
        string.strip()
        re.sub('[^A-Za-z0-9]+', '',string)
        dictt = {}
        dictt = invertedIndexx(string.lower(),i)
        myfile.close()
        for x,y in dictt.items() :
           if tokens.get(x) == None:
                tokens.update({x:[]})
           tokens[x].extend(y)
    
    return tokens


def invertedIndexx(string,j): 
    s=''
    tokens = {}
    for i in range(len(string)) :
        if string[i] != ' ' and string[i].isalnum():
            s=s+string[i]
        elif s!= '' :
                
            if tokens.get(s.lower()) == None :
                    tokens.update({s.lower():[]})
            tokens[s.lower()].append(j+1)
            tokens[s.lower()] = unique(tokens[s.lower()])
            s=''
    
    return tokens 