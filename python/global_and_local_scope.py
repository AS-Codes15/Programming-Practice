a=20                 #global
"""def display():
    a=3              #local
    print(a)
display()
print(a)    """

"""def display():
    a=3
    def show():
        print(a)
    show()  
#show()             will give error

display()
print(a)    """

a,b=5,6
if a<b:
    c=a+b
print(c)                      # here it will not give any error but inside the function it will.bcoz of local scope of variable


