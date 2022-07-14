# Hierarchical Inheritance
# class Ineuron:
#     def iNeuron(self):
#         print("This is organization.")
#
#
# class Affilates(Ineuron):
#     def course(self):
#         print("This datascience course affilates to students.")
#
# class Jobathon(Ineuron):
#     def gotjob(self):
#         print("I am participating in jobathon and gotjob.")
#
# object1 = Affilates()
# object2 = Jobathon()
# object1.iNeuron()
# object1.course()
# object2.iNeuron()
# object2.gotjob()


# Hybrid Inheritance


class Ineuron:
    def func1(self):
        print("This function is in iNeuron.")

class Hackathon(Ineuron):
    def func2(self):
        print("This function is in hackathon. ")


class Jobathon(Ineuron):
    def func3(self):
        print("This function is in jobathon.")


class Gotjob(Jobathon, Ineuron):
    def func4(self):
        print("This function is in gotjob.")


object = Gotjob()
object.func1()
object.func3()
object.func4()