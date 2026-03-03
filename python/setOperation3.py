set1={1,2,3,4,5,6,8,0}
set2={0,2,4,6,8}

"""print(set1.isdisjoint(set2))                           #return true if nothing is common
print(set1.isdisjoint((6,7,8)))"""

"""print(set1.issubset(set2))
print(set1.issubset([1,2,3,4,5,6,7]))
print(set1 <= set2)                                      # for checking subset

print(set1.issuperset(set2))
print(set1 >= set2)"""

#set2.clear()                                             #dlt all element of set
del set2                                                  # dlt element as well as set also
print(set2)