class Circle:
    pi=3.14                                # class object variable
    def __init__(self,r) :
        self.radius=r
    def circum(self):
        return 2 * self.pi * self.radius
    def area(self):
        return self.pi * self.radius**2
    
Circle1=Circle(4)    
print(Circle1.circum())
print(Circle1.area())
        