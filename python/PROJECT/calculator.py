import os
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b

operations_dict={
    "+" : add,
    "-" : sub,
    "*" : mult,
    "/" : div
}
def calculator():
    num1=float(input("Enter first number: "))
    for symbol in operations_dict:
        print(symbol)

    continue_flag=True
    while continue_flag:
        operator=input("pick an operation: ")  
        num2=float(input("Enter second number: ")) 
        calculator_function=operations_dict[operator]
        output=calculator_function(num1,num2)
        print(f"{num1} {operator} {num2} = {output}")
        should_continue=input(f"enter 'y' to continue with {output} or 'n' to start new calculation or 'x' to exit").lower()
        if should_continue=='y':
            num1=output
        elif should_continue=='n':
            continue_flag=False
            os.system('cls')
            calculator()   
        else:
            continue_flag=False
            print("Bye")
calculator()  