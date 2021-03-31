from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from .ComplexProcessing import ComplexQUeryFunc
import json
# Create your views here.
def ComplexQUery(request,queryy) :
    
    with open("InvertedIndex.json", 'r') as ii:
        Inverted_index = json.load(ii)

    

    data = ComplexQUeryFunc(Inverted_index ,queryy)
    
    sr = {
        'value':data
    }
    return render(request,'ComplexQuery.html',sr)
