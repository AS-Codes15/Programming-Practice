import math
def primeChecker(number):
    isPrime=True
    if number==1:
        isPrime=False
    for i in range(2,math.ceil(number/2)+1):                # for i in range(2,number):  
        if number%i == 0:
            isPrime=False
    if isPrime==True:
        print("Number is prime")
    else:
        print("Number is not prime") 
n=int(input("Enter the number to check:\n"))
primeChecker(n)           

        
