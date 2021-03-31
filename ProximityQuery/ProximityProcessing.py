from BooleanModelIR.QueryProcessing import Convert
from complexQuery.Operations import ANDD
def Proximity_Query_func(posIndex,quer) :
    #initialized
    retrivedDoc = {}
    dictt = {}
    lst_Common = []
    
    query = Convert(quer)
    #Logic For each Term 
    query3 = query[2]
    kdiffernece = (int(query3[1:])+1)
    query.pop(2)
    for term in query :
        try:
            dictt.update({term:posIndex[term]})
        except KeyError :
             dictt.update({term:[]})
    lst_Common = ANDD(dictt[query[0]],dictt[query[1]]) #Doing And operation on both terms-DocID
    
    #Maintaining the list of both DocID
    lst1 = {}
    lst2 = {}
    for i in lst_Common :
      lst1.update({i :posIndex[query[0]][i]})

      lst2.update({i :posIndex[query[1]][i]})
    
    #Search for the closest pair 
    #using o( n^2 + m )
    res = []
    jj=0
    ii=0
    f1 = False
    for i in lst_Common :
      for j in range(len(lst1[i])):
        for k in range(len(lst2[i])) :
          if abs(lst1[i][j] - lst2[i][k]) == kdiffernece :
            res.append(i)
            f1 = True 

    if f1 :
      return res 
    return -1

