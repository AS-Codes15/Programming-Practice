"""def display(name,department):
    print(f"Hii {name}, are you from {department} department")
display("Archu","CS")                                             #positiobal argument
display(department='CS',name='Archu')                              #keyword argu
display('Archu',department='CS')                                  #combination of positional and keyword (keyword argument sould follow posional argument) 
"""

# default argument should be provided after nan default
"""def greet(name,subject,dept='CS'):                              
    print("Hii", name)
    print(f"do you teach {subject}")
    print(f"are you from {dept} department")
greet('Archu','Python')                                          #dept is default argument
greet('Archu','Python','IT')                                     #over write the value of dept"""

# Arbitrary argument
def add(*numbers):                                                #tuple of many number(used when number of argument is not known)
    sum=0
    for i in numbers:
        sum+=i
    print(f"sum is: {sum}")
add(5,8,5)    
add(4,4,10,20)

            
