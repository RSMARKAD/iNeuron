
# Encapsulation
class Ineuron:
    def __init__(self):
        self.iNeuron = 'datascience'


class Affilates(Ineuron):
    def __init__(self):

        Ineuron.__init__(self)
        print("This course start from month of may: ",
              self.iNeuron)

        self.iNeuron = 'dataanalyst'
        print("This course start from month of june: ",
              self.iNeuron)


course1 = Affilates()

course2 = Ineuron()

print("I am affilates this course course1: ", course1.iNeuron)

print("I am doing this course course2: ", course2.iNeuron)

# Polymorphism

def add(a, b, c = 0):
    return a + b + c

print(add(3, 4))
print(add(3, 4, 5))


class Datascience():
    def python(self):
        print("python is part of data science course.")

    def sql(self):
        print("sql is a language and use in data science course .")

    def ml(self):
        print("ml is use in data science for model preparation.")


class Dataanalyst():
    def python(self):
        print("python is part of data analyst course.")

    def sql(self):
        print("sql is a language and use in data analysis.")

    def ml(self):
        print("ml is a out of syllabus of data analyst course.")


obj_ds = Datascience()
obj_da = Dataanalyst()
for course in (obj_ds,obj_da):
    course.python()
    course.sql()
    course.ml()

for course in (obj_da, obj_ds):
    course.python()
    course.sql()
    course.ml()