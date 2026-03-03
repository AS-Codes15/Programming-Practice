# loop control statements: 1. break
#                          2. continue
#                          3. pass
# used to terminate the loop
#used in for and while 


"""for i in range(1,101):
    if i==11:
        break
    else:
        print(i)
print("out from loop")        
      
      #OR

for i in range(1,100):
    print(i)
    if i==10:
        break
print("out from loop")"""

list1=["hii","hello","welcome"]
names=["ram","shyam","mohan"]
for item in list1:
    for name in names:
        print(item,name)
        if item=="hello" and name == "shyam":
            break
    print("out from inner loop") 
print("out from outer loop")       
