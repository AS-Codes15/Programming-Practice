# skip the particular

"""for i in range(1,11):
    if(i==7):
        continue
    else:
        print(i)"""
count=1
while count <=5:
    print( count)
    count+=1
    if count==4:
        continue
    print("hii")                       #skipped
print("out from loop")    