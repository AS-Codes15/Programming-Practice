"""student={
    "name" : "Ram",
    "subject" : {
        "phy": 90,
        "chem": 80,
        "math": 90   
    }
}
print(student)
print(student["subject"]["phy"])"""

"""student_data={
    "Ram" : {"roll_no" : 19,"age": 20,"course": "python"},
    "Mohan" : {"roll_no" : 20,"age": 22,"course": "java"}
}
#print(student_data["Ram"])
#print(student_data)

student_data["Ram"]["phone_no"]=7935
print(student_data["Ram"])

#del student_data["Ram"]["phone_no"]
print(student_data["Ram"].pop("phone_no"))
print(student_data["Ram"])
"""
"""travel_data={
    "Gujrat" : ['Dwarka','Somnath','Statue of unity'],
    "Rajasthan" : ['Jaipur','Udaipur']
}
print(travel_data)"""

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
       "phone_no" : [1234,5678]
    }
]
print(student_data)
print(student_data[0])
print(student_data[1]["phone_no"])
