# print is function and return is a keyword
# print can be used anywhere in the program whereas the return can only be used within the function
# return value can be further used but print value can be used later

"""def add1(a,b):
    c=a+b
    print(c)
add1(4,9)"""

def add1(x):
    return x+1
def add2(a,b):
    c=a+b
    return c
result2=add2(4,9)
final_result=add1(result2)
print(final_result)