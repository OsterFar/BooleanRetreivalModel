from django.shortcuts import render,HttpResponse,redirect
from .QueryProcessing import QuerySelection,Convert
from .classQuery import Query
from .InvertedIndex import tokenization_caseFoldingg
from .Preprocessing import StopWordsRemoval
from .PositionalIndex import Positional_index
import json 
def home(request):
  
   
    if request.method == 'GET' :
        
        #----------------------------
        #Making Inverted Index 
        #-----------------------------
        
        try :
            with open('InvertedIndex.json', 'r') as ij:
                #json.load(ij)
                ij.close()
            print("\n\nyes")
            
        except FileNotFoundError :
            invertedIndex  = tokenization_caseFoldingg()
            invertedIndex = StopWordsRemoval(invertedIndex)
            print(invertedIndex['passenger'])
            print("\n\n\nWord ====",invertedIndex['smiling'])

            
            with open('InvertedIndex.json', 'w') as ij:
                json.dump(invertedIndex,ij)
                ij.close()
            print("no")

        #-------------------------
        #invertedIndex Ends Here 
        #--------------------------

        #-------------------------------------------------------------

        #------------------------------------
        #Positional Index starts from here 
        #--------------------------------------



        try :
            with open('Positional_index.json', 'r') as ij:
                #json.load(ij)
                ij.close()
            print("\n\nyes_pos")
            
        except FileNotFoundError :
            pos_index = Positional_index()
            print(pos_index)
            print("\n\n\nWord ====",pos_index['smiling'])

            
            with open('Positional_index.json', 'w') as ij:
                json.dump(pos_index,ij)
                ij.close()
            print("no_pos")
        
    
    else :
        queryStr = request.POST['QueryVal']
        querylist = queryStr.strip()
        retObj  = QuerySelection(querylist)
        return redirect('{0}'.format(retObj.method),queryy=retObj.queryName)
    return render(request,'home.html')



def complx(request) :
    print("Hey there ")
    return HttpResponse("hello word")

def ComplexQUery(request,methodd,queryy) :
    print(methodd,"\n\n",queryy)
    return HttpResponse("hello word Good day \n data = {0} \n\n {1}".format(methodd,queryy))
def okey(request) :
    return render(request,'index.html')