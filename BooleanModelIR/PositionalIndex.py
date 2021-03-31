
#-------------------------------
# Postional Index
#-------------------------------
import nltk
from nltk.tokenize import RegexpTokenizer


def Positional_index():
  dictt= {}
  for i in range(1,51) :
      myfile = open('AllFiles/{0}.txt'.format(i), encoding='utf-8')
      #Pre Processing For Positional indexes
      string  = myfile.read()
      string = string.lower()
      tokenizer = RegexpTokenizer(r'\w+')
      lst = tokenizer.tokenize(string)

      #logic
      for j in range(len(lst)) :
        if dictt.get(lst[j]) == None :
          dictt[lst[j]] = {}
        if dictt[lst[j]].get(i) == None  :
          dictt[lst[j]].update({i:[]})
        dictt[lst[j]][i].append(j)
  return dictt
      
