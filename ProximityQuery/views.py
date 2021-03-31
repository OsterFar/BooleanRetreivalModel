
from django.shortcuts import render,HttpResponse,redirect
import json
from .ProximityProcessing import Proximity_Query_func
# Create your views here.
def Proximity_Query(request,queryy) :
    
    with open("Positional_index.json", 'r') as ii:
        Positional_index = json.load(ii)

    #print("\n\n\n\n\n " , Positional_index['possible'],"\n\n\n")
    data = Proximity_Query_func(Positional_index , queryy)
    
    #for i in data :
    print(type(data))
    print
    if data != '-1' or str(data) > str(1):
    
        print(data)
        for i in data :
            print("=============i========",i)
            myfile = open('AllFiles/{0}.txt'.format(int(i)+1), encoding='utf-8')
            string  = myfile.read()
            #string= list(string.split())
            sr = {
                'st'.format(i):string
            }
            
    else :
        content = {
            error : "value Not FOund "
        }
        
    sr.update({'value':data})
    
   
    print(sr)
    #print(content)
    return render(request,'Proximity.html',sr)


    
