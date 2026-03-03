student_data=[                                                                  #dictionary within a list
   {
       "name": "Ram",
       "roll_no" : 19,
       "age": 20,
       "course": "python"
    },
   {
       "name" : "Mohan",
       "roll_no" : 20,
       "age": 22,
       "course": "java",
    }
]
def add_new_student(name,roll_no,age,course):
    new_student={}
    new_student["name"]=name
    new_student["roll_no"]=roll_no
    new_student["age"]=age
    new_student["course"]=course
    student_data.append(new_student)
add_new_student("Shyam",21,24,"C++") 

print(student_data)   
print(student_data[0])
print(student_data[1])
print(student_data[2])
print(student_data[1]["name"])

   

