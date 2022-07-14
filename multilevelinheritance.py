# class Grandfather:
#
#     def __init__(self, gname):
#         self.gname = gname
#
# class Father(Grandfather):
#     def __init__(self, fathername, gname):
#         self.fathername = fathername
#         Grandfather.__init__(self, gname)
#
# class Son(Father):
#     def __init__(self, sonname, fathername, gname):
#         self.sonname = sonname
#         Father.__init__(self, fathername, gname)
#
#     def print_name(self):
#         print('Grandfather name :', self.gname)
#         print("Father name :", self.fathername)
#         print("Son name :", self.sonname)
#
#
# s1 = Son('Martand', 'Ravikiran', 'Shankar')
# print(s1.gname)
# s1.print_name()


class Ineuron:

    def __init__(self, iNeuron):
        self.iNeuron = iNeuron

class Course(Ineuron):
    def __init__(self, datascience, iNeuron):
        self.datascience = datascience
        Ineuron.__init__(self, iNeuron)

class Jobathon(Course):
    def __init__(self, datascientist, datascience, iNeuron):
        self.datascientist = datascientist
        Course.__init__(self, datascience,iNeuron)

    def print_name(self):
        print('Organization  name :', self.iNeuron)
        print("Course name :", self.datascience)
        print("Post name :", self.datascientist)


j1 = Jobathon('datascientist', 'datascience', 'iNeuron')
print(j1.iNeuron)
j1.print_name()