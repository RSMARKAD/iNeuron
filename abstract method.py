from abc import ABC, abstractmethod

class Ineuron(ABC):

    def move(self):
        pass

class Datascience(Ineuron):

    def move(self):
        print("I can doing this course")

class Dataanalyst(Ineuron):

    def move(self):
        print("I can affilates this course")

class Blookchain(Ineuron):

    def move(self):
        print("I course start in iNeuron by telasku")

class Sql(Ineuron):

    def move(self):
        print("This is community course and started in iNeuron ")


DS = Datascience()
DS.move()

DA = Dataanalyst()
DA.move()

BC = Blookchain()
BC.move()

SQ = Sql()
SQ.move()

from abc import ABC, abstractmethod


class Animal(ABC):

    def move(self):
        pass


class Human(Animal):

    def move(self):
        print("I can walk and run")


class Snake(Animal):

    def move(self):
        print("I can crawl")


class Dog(Animal):

    def move(self):
        print("I can bark")


class Lion(Animal):

    def move(self):
        print("I can roar")


# Driver code
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()