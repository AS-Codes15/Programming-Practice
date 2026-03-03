# multiple data in single variable
# sets are unordered so the indexing in not allowed
# duplicates items (repition of item) are not allowed 
# slicing is not allowed
# itmes are inmutable (unchangable) but can be removed and added

set1={2,5,2,3,'archana',True,1}
"""set2=set()
print(type(set1))
print(type(set2))
print(set1)
print("length of set1 is: ",len(set1))"""

"""set1.add(19)
print(len(set1))"""

"""set1.discard(44)
print(set1)"""
#print(set1.pop())

#set1.add([2,3,4])      not allowed

set1.add((45,18,93))
print(set1)