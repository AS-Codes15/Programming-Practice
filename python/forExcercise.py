# program to calculate average height from list of heights

heights=input("enter the all heights seperatd by space: ")
height_list=heights.split()
count=0

for height in height_list:
    count=count+1
print(count) 

for i in range(count):
    height_list[i]=int(height_list[i])
print(height_list) 

total=0
for height in height_list:
    total+=height
avg=total/count
print(round(avg))    