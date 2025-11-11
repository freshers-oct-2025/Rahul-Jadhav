from abc import ABC, abstractmethod

class Computer:
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):

    def process(self):
        print("it's running")

lap1=Laptop()
lap1.process()


