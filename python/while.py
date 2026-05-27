# used to execute a set of statements untill a given condition is satisfied
# in while else, else will be executed when the loop contion will be false
# else will not be executed when there is any break or any other terminating keyword
#used when we dont know how many times the loop will be executed
# value used to terminate the loop:  Sentinel value (-1, N, q)

"""count =1
while count <= 5:
    print(count)
    count+=1
print("out from loop")"""

"""count=5
while count > 0:  print(count); count-=1
print("out of loop")"""

"""count=1
while count < 5:
    print(count)
    count+=1
else:
    print("in else block")
print("out from loop")   
"""

"""count=1
while count < 6:
    print(count)
    count+=1
    if count==4:
        break
else:
    print("in else block")
print("out from loop")    
"""
"""number=int(input("enter a number(-1 for quit)"))
while number!=-1:
    print(number)
    number=int(input("enter a number(-1 for quit)"))
else:
    print("in else block")    
print("out from loop")
"""

"""count=1
while count < 1:
    print(count)
    count+=1
else:
    print("in else block")
print("out from loop")    """

"""count=0
while True:
    print(count)
    count+=1 
    if count==5:
        break
else:
    print("welcome to else block")
print("out from loop")        """

total=0
number=int(input("enter a number(0 to quit)"))
while number!=0:
    total+=number
    number=int(input("enter a number(0 to quit)"))
print(total)    
