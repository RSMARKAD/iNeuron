# This is OOPS Class

class MyClass:
  x = 'Data science'

p1 = MyClass()
print(p1.x)

class Company:
    c='iNeuron'

c1=Company()
print(c1.c)

class Student:
    s=20

s1=Student()
print(s1.s)

class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

e1 = Employee("Ravi", 1001)

print(e1.name)
print(e1.id)


class Company:
    def __init__(self,name,year):
        self.name = name
        self.year=year

c=Company("iNeuron", 4)
print(c.name)
print(c.year)

class Course:
  def __init__(self, name, duration):
    self.name = name
    self.duration = duration

  def myself(self):
    print("Im doing course in " + self.name)
    print("This course finish in month"+ self.duration)

c1 = Course("iNeuron", 12)
print(c1.name)
print(c1.duration)

class Course:
    def __init__(self, name, affilates):
        self.name=name
        self.affilates=affilates

    def iNeuron(self):
        print("Name of the running course" + self.name)
        print("I am affilated this course to no. of person="+self.affilates)

x=Course("Data analyst",5)
print(x.name, x.affilates)