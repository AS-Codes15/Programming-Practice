set1={'archu','arshi','divya'}
set2={'archu','anchal','jaya'}
set3={'manya','raunu'}

#print(set1.union(set2))
#print(set1 | set2)

#print(set1.union(set2,set3))
#print(set1 | set2 | set3)

#print(set1.union(('ram','shyam')))

#set1.update(set2)  
#set1.update([3,4,5])

#set1 |= set2                    
#print(set1)

#intersection

"""print(set1.intersection(set2))
print(set1.intersection(set2,set3))"""

#print(set1 & set2)

#print(set1.intersection(set2))

"""set2.intersection_update(set1)
print(set1)
print(set2)
"""
set2.intersection_update(['ram','shyam'])
print(set2)