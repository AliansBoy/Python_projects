from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):  #Can't create exempl of abstract class
    def walk(self):
        print('Walking...')

    @abstractmethod
    def num_legs(self):  #All children classes must have this method
        pass


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 4


class Monkey(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 2


animals = [Dog('Rolf'), Monkey('Bob')]
for a in animals:
    print(isinstance(a, Animal))
    print(a.num_legs())
