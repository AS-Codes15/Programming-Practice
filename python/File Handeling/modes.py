"""f1=open("file_1.txt","r")                         # if file does not exits, it will give error
data=f1.read()
print(data)
"""
#f1=open("file_1.txt","w")                            # will erase or override the content of file 1


#f1=open("file_1.txt","w")                          # if file does not exist, it will create it 

"""f1=open("file_1.txt","r+")                          #  will not create file if not exists
print(f1.tell())

#print(f1.read())
#f1.write(" keep going")

f1.write("hi")                                     # override at the begining
print(f1.tell())
print(f1.read())
print(f1.tell())
"""
