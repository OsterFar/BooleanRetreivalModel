def ANDD(lst1, lst2):
    return list(set(lst1) & set(lst2))

def ORR(lst1, lst2):
    final_list = lst1 + lst2
    return final_list

def NOT(lst2) :
    universal =[i+1 for i in range(50)]
    
    not_list = set(universal) ^ set(lst2)
    return list(not_list)