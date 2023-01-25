# 25.4 ABSTRACT BASE class

from abc import ABCMeta, abstractmethod 

class Shape(metaclass = ABCMeta): # No OBJECT from abstract class can be created
    @abstractmethod
    def area(self):
        return 0

class Rect(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.len = 6
        self.brd = 10
    def area(self):
        return self.len * self.brd

re = Rect()
print(re.area())
