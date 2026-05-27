# random module is inbuilt module in python
# used to genrate sudo random number

import random
#a=random.randint(1,4)
#a=random.randrange(1,3)         #3 is not included
#a=random.random()               #for floating point no.
#a=random.uniform(3,5)            #floating point in range
a=[1,2,3,4,5,6]
#print(random.choice(a))
random.shuffle(a)
print(a)