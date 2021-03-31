from django.shortcuts import render , HttpResponse
from .simpleProccesing import SimpleQueryy
import json 

# Create your views here.
def SimpleQuery(request,queryy) :
  
    
    with open("InvertedIndex.json", 'r') as ii:
        Inverted_index = json.load(ii)

    #print("\n\n\n\n\n " , Inverted_index['permission'],"\n\n\n")
    
    #data = ComplexQUeryFunc(Inverted_index ,queryy)
   
    data = SimpleQueryy(Inverted_index ,queryy)
    lst2 = []
    listt = []
    print(data)
    for i in data :
        listt.append(i)
        lst2 = data[i]
    print("-==-352=3=============")    
    print(listt , "\n\n" ,lst2)
    sr = {
        'value':lst2,
        'key':listt
    }
    return render(request,'SimpleQuery.html',sr)
