# global keyword is used to modify global variables
# used to create any global variable inside the function or from a non global space

"""a=10
def display():
    global a
    a=a+1
    print(a)

display()
print(a)"""

def display():
    a=20
    def show():
        global a
        a=40
    print(f"value of a before calling the show function is: {a} ") 
    show()
    print(f"value of a after calling the show function is: {a} ") 

display()
print(a)

name="archana"
def display():
    global name
    name= name+"sharma"
print(name)
display()
print(name)    
