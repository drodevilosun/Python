
class Animal(object):
    def __init__(self, Animal_name):
        self.name = Animal_name
        print("%s very cute and very loyal" %(self.name))

class Dog(Animal):
    def __init__(self):
        print("Dog has 4 legs")
        super().__init__("Dog")

d1 = Dog()