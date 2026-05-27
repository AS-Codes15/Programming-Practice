import math
def cans(height,width,coverage):
    area=height*width
    no_of_cans=math.ceil(area/coverage)
    print(f"number of cans: {no_of_cans}")
h=int(input("enter the value of height: "))    
w=int(input("enter the value of width: "))  
cover=7
cans(height=h,width=w,coverage=cover)  
