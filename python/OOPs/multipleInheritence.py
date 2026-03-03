# 1 subclass and more than aone superclass

class Student:
    def __init__(self) -> None:
        print("calling init from student")
        
    def reading(self):
        print("i can read")
    def writing(self):
        print("i can write")     

class Girls:
    def sing(self):
        print("i can sing a song")
    def writing(self):
        print("i can write technical reports")     

class GirlStudent(Student,Girls):                                  # ordering of parent class is important
    def sing(self):
        print("he sings")

obj=GirlStudent()
"""#obj.reading()
#obj.sing()
obj.writing()                                        # will access from the firstly inhereted superclass
#Girls.writing(obj)                                 # will acess writing method from the written superclass

print(GirlStudent.mro())
"""