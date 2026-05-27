f1=open("file_2.txt","w+")
print(f1.tell())
f1.write("hii welcome")
print(f1.tell())
f1.write("this is python course")
print(f1.tell())
#data=f1.read()
#print(data)                                 # will not print anything bcoz after the above operation the pointer will be at last position

f1.seek(0)
print(f1.tell())
data=f1.read()
print(data)
print(f1.tell())
f1.close