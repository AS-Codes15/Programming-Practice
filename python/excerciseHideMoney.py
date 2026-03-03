row1=[1,2,3]
row2=[2,3,4]
row3=[3,4,5]
matrix=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=(input("enter the position where you want to hide the money"))
row_number=int(position[0])
column_number=int(position[1])
row_selected=matrix[row_number-1]
row_selected[column_number-1]='X'
print(f"{row1}\n{row2}\n{row3}")