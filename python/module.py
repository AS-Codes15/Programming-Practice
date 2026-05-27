"""import my_module
print(my_module.a)
print(my_module.square_area(4))"""

"""import my_module as m                                 # to give name(m) to the module to import
print(m.a)
print(m.square_area(4))"""

"""from my_module import calculator,a                       # to import only specific thing from module
print(a)
calculator(3,2)"""

#from my_module import calculator  as c
#c(3,2)

"""from my_module import *                                  # to import all thing
print("value of a from another module is: ",a)
print(square_area(4))
calculator(3,2)"""

import my_module
a,b=3,1
sum=a+b
print("sum is: ",sum)
print("value of a from another module is: ",my_module.a)