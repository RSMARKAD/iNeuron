# class Mother:
#
#     def mother(self,mothername):
#         self.mothername=mothername
#
# class Father:
#
#     def father(self,fathername):
#         self.fathername=fathername
#
# class Son(Mother, Father):
#
#     def sonname(self,sonname):
#         self.sonname=sonname
#
#     def parents(self):
#         print("Father :", self.fathername)
#         print("Mother :", self.mothername)
#         print("Son Name:",self.sonname)
#
#
# s1 = Son()
# s1.fathername = "RAVIKIRAN"
# s1.mothername = "NIKITA"
# s1.sonname="MARTAND"
# s1.parents()

#
# class Mother:
#
#     def __init__(self,mothername):
#         self.mothername=mothername
#
# class Father:
#
#     def __init__(self,fathername):
#         self.fathername=fathername
#
# class Son(Mother, Father):
#
#     def __init__(self,sonname,fathername,mothername):
#         self.sonname=sonname
#         Father.__init__(self,fathername)
#         Mother.__init__(self,mothername)
#
#     def parents(self):
#         print("Father :", self.fathername)
#         print("Mother :", self.mothername)
#         print("Son Name:", self.sonname)
#
#
# s1 = Son("RAVIKIRAN", "NIKITA", "MARTAND")
# s1.parents()


class Organization:

    def iNeuron(self,iNeuron):
        self.iNeuron=iNeuron

class Datascience:

    def datascience(self,datascience):
        self.datascience=datascience

class Oops(Organization,Datascience):

    def oops(self,inheritance):
        self.inheritance=inheritance

    def course(self):
        print("Organization Name :", self.iNeuron)
        print("Course Name :", self.datascience)
        print("Topic Name :",self.inheritance)


o1 = Oops()
o1.iNeuron = "iNeuron"
o1.datascience = "datascience"
o1.inheritance="Inheritance"
o1.course()