class Student:
    def __init__(self,pen):
        self.books=1
        self.notebooks=5
        self.pens=pen
    def reading(self):
        print("i can read")
    def writing(self):
        print("i can write")    

class Girl(Student):
    def __init__(self,name,no_of_pens):
        super().__init__(no_of_pens)
        self.name=name

    def sing(self):
        print("i can sing a song")
        
    def writing(self):      
       super().writing()                                       
       print("i can write technical reports")  

    def display(self):
        print(f"Hii, I am {self.name}. I have {self.books} book, {self.notebooks} notebook and {self.pens} pens")   


Girl_1=Girl("Amayra",2)
"""Girl_1.reading()
Girl_1.writing()
Girl_1.sing()"""

print(Girl_1.name)
print(Girl_1.books)
print(Girl_1.notebooks)
print(Girl_1.pens)
print(Girl_1.display())