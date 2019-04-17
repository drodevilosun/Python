#override
class Parent(object):
    def override(self):
        print ("PARENT override()")

class Child(Parent):
    def override(self):
        print ("CHILD override()")

dad = Parent()
child = Child()

dad.override()
child.override()
