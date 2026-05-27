#  *args: arbitrary positional argument
#  **kwargs:  arbitrary keyword argument
#  *args always should be pass before **kwargs

# ARBITRARY POSITIONAL ARGUMENT
"""def add(*numbers):                              #tuple of many number(used when number of argument is not known)
    sum=0
    for i in numbers:
        sum+=i
    print(f"sum is: {sum}")
add(5,8,5)    
add(4,4,10,20)"""

"""def add(*numbers,name):                                                 
    sum=0
    print(numbers)
    print(name)
    for i in numbers:
        sum+=i
    print(f"sum is: {sum}")
add(5,8,5,name="Archa")    
"""

"""def add(a,*numbers):                                                 
    sum=0
    print(numbers)
    print(a)
    for i in numbers:
        sum+=i
    print(f"sum is: {sum}")
add(2,5,8,5)    
"""

# ARBITRARY KEYWORD ARGUMENT
"""def info_person(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
info_person(name='Archu',age=20,dept='CS')
info_person(name='Archana',age=20,dept='CS')
"""
def info_person(*args,**kwargs):
    for key,value in kwargs.items():
        print(key,value)
    print(args)    
info_person(2,4,name='Archu',age=20,dept='CS')
info_person(1,3,5,name='Archana',age=20,dept='CS')

