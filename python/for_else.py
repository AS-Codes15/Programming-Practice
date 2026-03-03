# else block will execute if the for loop is completed successfully
# if there is any break in the loop then the else block will not be executed

tuple=(2,4,6,8,10,12)
"""for i in tuple:
    print(i)
else:
    print("loop has been completed successfully and we are in else block now")    
"""
"""for i in tuple:
    print(i)
    if i==8:
        break
else:
    print("loop has been completed successfully and we are in else block now")   """ 

for i in tuple:
    if i%11==0:
        print(i)
        break
else:
    print("there is no number in sequence divisible by 11")