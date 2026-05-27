set1={'archu','arshi','divya','manya'}
set2={'archu','anchal','jaya'}
set3={'manya','raunu'}

"""
print(set1.difference(set2))
print(set1.difference(('ram','shyam')))
print(set1.difference(set2,set3))
print(set1 - set3)"""

"""##set1.difference_update(set2)
##print(set1)
set2.difference_update(set1)
print(set2)"""

print(set1.symmetric_difference(set2))                 #not allowed on different set
print(set1 ^ set2 ^ set3)                               # can apply on multiple set

set2.symmetric_difference_update(set1)
print(set2)
set1.symmetric_difference_update(('archu','manya'))
print(set1)