# used to store multiple items in a singlr variable
# mix data types are allowed
# declaration:   tuple=(1,2,3)
#                tuple=(10,)
# tuples are inmutable
# nesting of tuples are allowed
# a list can be converted into tupple

tuple1=(12,6,-8,'Archana',True,12,6)
tuple2=(10,20,30)
tuple3=(tuple1,tuple2)

"""print(tuple3)
print(tuple3[0])
print(len(tuple3))                               
tuple3=tuple1 + tuple2
print(len(tuple3))                                
"""

"""print(tuple1.index(12))
print(tuple1.count(6))
print(min(tuple2))
print(max(tuple2))"""

"""print(tuple1[0:3])                            #slicing
print(tuple1[::2]) """ 

#print(len(tuple1))

"""print(tuple1[-2])
print(type(tuple1))"""

#tuple2=(10,)
#print(type(tuple2))

"""list1=[19,30,1]
print(tuple(list1))
"""

tuple4=(10,)*5
print(tuple4)
