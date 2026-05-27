# used to generate series of integers
# syntax:     range(begin,end,step)
# end is mandatory 
# end in not included in the generated series
# degault value of begin is 0 and step is 1

"""a=range(5)
# print(a[0],a[1],a[2],a[3],a[4])
for i in a:
    print(i)
"""
"""a=range(1,1)
for i in a:
    print(i)"""

"""for i in range(10,0,-1):
    print(i,end=" ")
print()

for i in range(65,91):
      print(chr(i),end=" ")  """
sum=0
for i in range(2,11,2):
    sum=sum+i
print(sum)    

