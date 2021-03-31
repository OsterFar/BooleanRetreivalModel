from .classQuery import Query



def QuerySelection(query) :
    
    MAX = 10000 # imagine the max word apart will be 
    # //query = []
    # //query = Inputt()
    f1 = False 
    f2 = False 
    
    operators = ['and','or','not']
    for i in range(3) :
        if operators[i] in query :
            f1= True
            break 
    
    st = str(query[ len(query)-1 ])
    s = "\\"
    print('\n\nMy vALUE = ',st,'\n')
    if(st.isnumeric() ):
        f2 = True 
    
    #forming Simple QUeries
    #remember this query is not used with and or not 
    
    if f1 == False and f2 == False : 
    #print(SimpleQuery(query))
        retObj = Query(query,"SimpleQuery")
    elif f1 == True :
    #print(ComplexQUery(invertedIndex))
        retObj = Query(query,"ComplexQUery")
    
    else :
    #print(Proximity_Query(pos_index,query)) 
        retObj = Query(query,"Proximity_Query")
    
    return retObj

#input Queries
def Inputt() :
    querystring = "Word and best not good"
    query= Convert(querystring)
    return query

#string to list converter
def Convert(string):
    li = list(string.split(" "))
    return li
