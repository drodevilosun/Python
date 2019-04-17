#Using Supper for inheritance. EX: Alter Before or After

class Parent(object):
    def Alter(self):
        print ("PARENT Alter()")

class Child(Parent):
    def Alter(self):
        print("CHILD, BEFORE PARENT Alter()")
        super(Child,self).Alter()
        print ("CHILD, AFTER PARENT Alter()")

dad = Parent()
child = Child()

dad.Alter()
child.Alter()
