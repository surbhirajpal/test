#Q1
class Animal:
    def animal_attribute(self):
        a=input("enter name of animal ")
        print("entered animal is %s"%a)
class Tiger(Animal):
    def tiger_attribute(self):
        self.animal_attribute()
t=Tiger()
t.tiger_attribute()

#Q2
#AB
#AB


#Q3
class Cop:
    def __init__(self,name,age,work,desig):
        self.n=name
        self.a=age
        self.w=work
        self.d=desig
    def add(self):
        self.n = input("enter name : ")
        self.a = int(input("enter age : "))
        self.w = int(input("enter work experience : "))
        self.d = input("enter designation : ")
    def display(self):
        print("name is %s"%self.n)
        print("age is %d years"%self.a)
        print("work experience is %d years"%self.w)
        print("designation is %s"%self.d)
    def update(self):
        self.n=input("enter updated name : ")
        self.a=int(input("enter updated age : "))
        self.w=int(input("enter updated work experience : "))
        self.d=input("enter updated designation : ")
class Mission(Cop):
    def add_mission_details(self):
        self.add()
        self.display()
        self.update()
        self.display()
c=Cop('',0,0,'')
m=Mission('',0,0,'')
m.add_mission_details()



#Q4
class Shape:
    def __init(self,length,breadth):
        self.l=length
        self.b=breadth
class Square(Shape):
    def area(self,length):
        return length*length
class Rectangle(Shape):
    def area(self,length,breadth):
        return length*breadth

s=Shape()
x=Square()
y=Rectangle()
length=int(input("Enter the length"))
breadth=int(input("Enter the breadth"))
side=int(input("Enter side of square"))
print("AREA OF SQUARE = ",(x.area(side)))
print("AREA OF RECTAGLE = ",(y.area(length,breadth)))