# two types of return: 1. Implicit    2. Explicit
# by default a function return "none"

"""def add(a,b):
    c=a+b
    #return 
    return c
   
#print(add(2,3))
result=add(5,6)
print(result)"""

def format_name(name,surname):
    formatted_name=name.title()
    formatted_surname=surname.title()
    return f"{formatted_name} {formatted_surname}"

formatted_name=format_name("archana","sharma")  
print(formatted_name)  