size=input("what size piza you want(s/m/l)?")
bill=0
if size=="s" or size=="S":
    bill+=100
    print("small pizza prize is 100")
elif size=='m' or size=='M':
    bill+=200
    print("medium pizza prize is 200")
else:
    bill+=300
    print("large pizza prize is 300")   
addPepperoni=input("do you want pepperoni(Y/N)?") 
if addPepperoni=='y' or addPepperoni=='Y':
    if size==" s" or size=="S":
        bill+=30
    else:
        bill+=50
extraCheese=input("do you want extra cheese(Y/N)?")        
if extraCheese=='y' or extraCheese=='Y':
    bill+=20
print(f"youe final bill is {bill} ")

    
