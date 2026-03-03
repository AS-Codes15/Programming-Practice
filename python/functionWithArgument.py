"""def add(a,b):
    print(f"the sum is: {a+b}")
add(5,7)
add(100,99) 
add(45,45)   """

"""def factorial(n):
    fact=1
    while(n>0):
        fact=fact*n
        n-=1
    print(f"factorial is: {fact}")  
n=int(input("enter the number: "))
factorial(n)      """

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(f"factorial of {n} is: {fact}")    
factorial(5)    