#abstraction
from abc import ABC , abstractmethod
class Vehicle(ABC):
    def drive(self):
        print("the vichle is started")
    @abstractmethod
    def start(self):
        pass 
class car(Vehicle):
    def start(self):
        print("car is started")
c1=car()
print(c1.start())
