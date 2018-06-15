#Q1

class Circle:
    def __init__(self,radius):
        self.r=radius
    def getArea(self):
        a=3.14*self.r*self.r
        print ("area of circle is : %s"%a)
    def getCircum(self):
        p=3.14*2*self.r
        print("circumference of circle is : %s"%p)
r=int(input("enter radius : "))
c=Circle(r)
c.getArea()
c.getCircum()


#Q2

class Student:
    def __init__(self,name,roll):
        self.n=name
        self.r=roll
    def display(self):
        print("name of student is %s"%self.n)
        print("roll number is %s"%self.r)
n=input("enter name : ")
r=input("enter roll number : ")
s=Student(n,r)
s.display()


#Q3

class temprature:
    def convertFahrenheit(self,c1):
        f1=float((c1*1.8)+32)
        print(" %2f celsius =%2f fahrenheit "%(c1,f1))
    def convertCelsius(self,f2):
        c2=float((f2-32)/1.8)
        print("%2f fahrenheit = %2f celsius "%(f2,c2))
t=temprature()
c1=float(input("enter temperature in celsius : "))
t.convertFahrenheit(c1)
f2=float(input("enter temperature in fahrenheit : "))
t.convertCelsius(f2)




#Q4
class MovieDetails:
    def __init__(self,movie,artist,year,rating):
        self.movie =movie
        self.artist=artist
        self.year=year
        self.rating=rating
    def display(self):
        print("name of movie is : %s "%self.movie)
        print("artist name is : %s "%self.artist)
        print("year of release is : %d "%self.year)
        print("ratings are : %s"%self.rating)
    def update(self):
        self.movie=input("update name of movie")
        self.artist=input("update artist name ")
        self.year=int(input("update year of release "))
        self.rating=input("update ratings ")
x=MovieDetails("raid","ajay devgun",2018,4.3)
x.display()
x.update()
x.display()




#Q5
class Expenditure:
    def __init__(self,expenditure,saving):
        self.ex=expenditure
        self.s=saving
    def display(self):
        print("expenditure is %d "%self.ex)
        print("savings are %d "%self.s)
    def totalSalary(self):
        self.t=self.s+self.ex
    def displaySalary(self):
        print("total salary is %d " % self.t)
a=int(input("enter expenditure "))
b=int(input("enter salary "))
x=Expenditure(a,b)
x.display()
x.totalSalary()
x.displaySalary()
