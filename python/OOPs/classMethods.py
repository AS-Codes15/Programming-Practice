class Instructor:
    followers=99                                                    # class object variable
    def __init__(self,name,address):
       self.name=name
       self.address=address 

    def display(self,subject):
        print(f"Hii, I am {self.name} and i am learning {subject}")   

    def updateFollower(self,followerName):
        self.followers+=1         

Instructor1=Instructor("Archana","Bangalore")
print(Instructor1.name,"",Instructor1.address)

Instructor1.display("python")
#print(Instructor1.display())

Instructor1.updateFollower("Archu")
print(Instructor1.followers)

Instructor2=Instructor("Archu","Bangalore")
Instructor2.updateFollower("Archana")
print(Instructor2.followers)
