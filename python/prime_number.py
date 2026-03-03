# to generate prime umber in range

"""lower=int(input("enter the lower range"))
upper=int(input("enter the upper range"))
print(f"Prime number between {lower} and {upper} including both are: ")
for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if num%i == 0:
                break
        else:
                print(num)
        """

# to check a no is prime or not

n= int(input("enter the number to check: "))
flag=False
if n==1:
    print(f"{n} is not a prime number")
elif n>1:
    for i in range(2,n):
        if n%i ==0:
            flag=True
            break
    if flag:
        print(f"{n} is not a prime number")
    else:
        print(f"{n} is a prime number") 
else:
    print("enter a positive number")               
