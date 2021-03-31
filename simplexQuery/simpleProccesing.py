#simple Queries 
from BooleanModelIR.QueryProcessing import Convert 

def SimpleQueryy(invertedIndex,quer) :
    print("\n\nKLesfjbasfngb=========================\n\n")    
    retrivedDoc = {} 
    
    query = Convert(quer)
    print("in simpleQuery : " ,query)
    #Using operator to check either user wrongly input operators in simple queries if so pass error
    operators = ['and','or','not']
    for i in range(len(query)):
        if query[i] not in operators :
            try:
                retrivedDoc.update({query[i]:invertedIndex[query[i]] })
            #retrivedDoc[query[i]].append( invertedIndex[query[i]])
            except KeyError:
                retrivedDoc.update({query[i]:[] })
        else : 
            raise Exception("Sorry, This is Simple query , operatores not allowed here use complex query instead")  

    return retrivedDoc


