def unique(list1):
 
    # intilize a null list
    unique_list = []
     
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    
    return unique_list


def StopWordsRemoval(token):
    myfile = open('Stopword-List.txt',encoding='utf-8')
    string = myfile.read()
    dictt = {}
    for x,y in token.items() :
        if x not in string.split() :
            if dictt.get(x) == None :
                dictt.update({x:[]})
        
            dictt[x].extend(y)
    myfile.close()
    return dictt
