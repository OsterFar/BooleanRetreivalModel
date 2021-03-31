 
from .ClassStack import Stack
from .Operations import ANDD, ORR , NOT
from BooleanModelIR.QueryProcessing import Convert

def ComplexQUeryFunc(inverted,quer) :

    #result set
    result = []
    queryy = Convert(quer)
    
    #using Stack Data Structure to process query
    stack_ds = Stack()
    #ExpectedOperators
    operators = ['and','or','not']
    count = 0 
    #print("===",queryy[0],inverted[queryy[0]])
    i = 0
    while ( i < (len(queryy)) ):
        if queryy[i] not in operators :

            ##TRY-Catch for if found not found in dict  
            try :
              stack_ds.push(inverted[queryy[i]])
            
            except KeyError :
              stack_ds.push([])
            i += 1
        else : 

          #====================================
          #Checking for AND Operator 
          #====================================
          if queryy[i] == operators[0] :
            if stack_ds.isEmpty != False :
              #pop from stack 
              eqn1 = stack_ds.top()
              stack_ds.pop()
              
              #print("from stack",eqn1)
              if queryy[i+1] == 'not' :
                #if the query  = "and not t1 "
                try :
                  eqn2 = NOT( inverted[queryy[i+2]] )
                except KeyError :
                  eqn2 = NOT([])
                i=i+2
              else :
                
                try :
                  eqn2 = inverted[queryy[i+1]]
                except KeyError :
                  eqn2 = []
                i=i+1 
            else :
              pass
            #Logic for And Operation
            result = ANDD(eqn1,eqn2)
            stack_ds.push(result)
            i +=1 
            #result is list = [] in which the andd values is stored

          #====================================
          #Checking for OR Operator 
          #====================================
          elif queryy[i] == operators[1] :
            if stack_ds.isEmpty != False :

              #pop from stack 
              eqn1 = stack_ds.top()
              stack_ds.pop()
              
              #print("from stack",eqn1)
              if queryy[i+1] == 'not' :
                #if the query  = "and not t1 "
                #try-Catch
                try :
                  eqn2 = NOT( inverted[queryy[i+2]] )
                except KeyError :
                  eqn2 = NOT([])
                i=i+2

              else :
                #try-Catch
                try :
                  eqn2 = inverted[queryy[i+1]]
                except KeyError :
                  eqn2 = []

                i=i+1 
            else :
              pass
            #Logic for And Operation 
            
            result = ORR(eqn1,eqn2)
            stack_ds.push(result)
            i +=1 

          #======================
          #NOT 
          #======================
          elif queryy[i] == operators[2]: 
            
            #try-Catch
            try :
              result = NOT( inverted[queryy[i+1]] )
            except KeyError :
              result = NOT([])

            stack_ds.push(result)
            i+=2


    return result 
