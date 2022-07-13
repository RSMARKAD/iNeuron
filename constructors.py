#Constructor and inheritance
class INeuron:

    # default constructor
    def __init__(self):
        self.iNeuron = "INeuron"

    # a method for printing data members
    def print_iNeuron(self):
        print(self.iNeuron)


# creating object of the class
obj = INeuron()

# calling the instance method using the object obj
obj.print_iNeuron()



class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Ravikiran", "Markad")
x.printname()


class Datascience:
    def __init__(self,name,tname):
        self.name=name
        self.tname=tname

    def print_name(self):
        print("All students doing course in"+ self.name)
        print("This course teach by" + self.tname)

d= Datascience ("ineuron", "sudhanshu")
print(d.name, d.tname)

