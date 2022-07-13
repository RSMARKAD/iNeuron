#Inheritance

class Datascience:
    def __init__(self,name,tname):
        self.name=name
        self.tname=tname

    def print_name(self):
        print("All students doing course in"+ self.name)
        print("This course teach by" + self.tname)

class Students(Datascience):
    def __init__(self,name, tname):
        Datascience.__init__(self, name, tname)


y=Students("ineuron", "sudhanshu")
y.print_name()


class Program:
    def __init__(self,hname,jname,fname):
        self.hname=hname
        self.jname=jname
        self.fname=fname

    def myself(self):
        print(self.hname, self.jname, self.fname)

class Participats(Program):
    def __init__(self, hname, jname, fname):
        Program.__init__(self, hname, jname, fname)

x=Participats("Hackathon","Jobathon", "iNeuron")
x.myself()


class Course:
    def __init__(self,name,lname):
        self.name=name
        self.lname=lname

    def print_name(self):
        print(self.name,self.lname)

class Students(Course):
    def __init__(self,name, lname):
        super().__init__(name, lname)

    def welcome(self):
        print("All students doing course of " + self.name)
        print("This course start of " + self.lname)


c=Students("datascience", "python")
c.welcome()
