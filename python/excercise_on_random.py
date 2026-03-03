import random
names=input("enter the name seperated by comma: ")
namesList=names.split(",")
length=len(namesList)
choice=random.randint(0,length-1)
print(f"{namesList[choice]} will pay the bill")
