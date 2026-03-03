"""for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()    
     """
        #OR

"""for i in range(1,6):                                   
    for j in range(1,i+1):                              
        print('*',end=" ")                            
    print()                                             
                  """                                    

n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()    
for i in range(n):
    for j in range(n-i-1):
        print("*",end=" ")
    print()    
