# To find fibonacci series upto nth term

num1=0
num2=1
n=int(input("enter the number of term: "))
if n<=0:
    print("enter the positive integer")
elif n==1:
    print(num1)  
else:
    print("Fibonacci series: ")
    print(num1,"\n",num2) 
    for i in range(3,n+1):
        nth=num1+num2
        print(nth)
        num1=num2
        num2=nth
