# __init__(self)         self is the reference to the current instance

"""class Student:
    def __init__(self,fullname):
       self.name=fullname
       print("adding new student in the database...")
s1=Student("ARCHANA SHARMA")
print(s1.name)
"""
class Instructor:
    def __init__(self,name,addres):
       self.name=name
       self.address=addres
       self.followers=99                                              #default value
Instructor1=Instructor("Archana","Bangalore")
print(Instructor1.name,"",Instructor1.address)
print(Instructor1.followers)