name1=input("enter your name: ")
name2=input("enter his/her name: ")
us=name1 + name2
lowerCaseName=us.lower()

t=lowerCaseName.count('t')
r=lowerCaseName.count('r')
u=lowerCaseName.count('u')
e=lowerCaseName.count('e')
true=t+r+u+e
l=lowerCaseName.count('l')
o=lowerCaseName.count('o')
v=lowerCaseName.count('v')
e=lowerCaseName.count('e')
love=l+o+v+e

love_score=int(str(true)+str(love))
if love_score < 30 :
    print(f"your love score is {love_score} so there is nothing ")
elif love_score >30 and love_score <= 40:
    print(f"your love score is {love_score}.It look like there is some chances")
elif   love_score >40 and love_score <= 60:      
    print(f"your love score is {love_score}.You guys are allright together") 
elif   love_score >60  and love_score <= 80:
    print(f"your love score is {love_score}. Looks like its a match ^_^") 
elif  love_score > 90:
    print(f"your love score is {love_score}.\n Made for each other")   
else:
    print(f"your love score is {love_score}")    