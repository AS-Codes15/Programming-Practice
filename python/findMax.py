numbers=input("enter teh numbers:")
number_list=numbers.split()
count=0

for number in number_list:
    count=count+1
print(f"the length of list is : {count}")    

for i in range(count):
    number_list[i]=int(number_list[i])

maximum_number=number_list[0]
for number in number_list:
    if number > maximum_number:
        maximum_number=number

print(f"maximum number is: {maximum_number}")       

