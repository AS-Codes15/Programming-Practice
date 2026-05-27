# syntax:
#            for varName in sequence:
#                    statement(s)
# used when we know the number of iteration

"""names=['ram','shyam','mohan']
for name in names:
    print(name)
    if name=='shyam':
        print("hello")"""

"""numbers=[2,3,4,5]
squares=[]
for i in numbers:
    square=i**2
    squares.append(square)
print(squares)          """

for i in range(1,6):
    for j in range(1,11):
        print(i*j,end=" ")
    print()    