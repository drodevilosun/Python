
class Parent(object):
    def try1(self):
        print("hello this is part 1")
    def try2(self):
        print("hello this is part 2")
    def try3(self):
        print("hello this is part 3")

class Child(Parent):
    def __init__(self):
        self.inherit = Parent
    def try1(self):
        self.inherit.try1(self)
    def override(self):
        print("CHILD override()")
    def altered(self):
        print("CHILD, BEFORE INHERIT altered()")
        self.inherit.try2(self)
        print("CHILD, AFTER INHERIT altered()")

overal = Parent()
son = Child()
son.try1()
son.override()
son.altered()

# def try1():
#     print("Hello")

# try1()