class Parent(object):
    def __init__(self):
        self.Create()

    def Create(self):
        print "Password"

class Child(Parent):
    def __init__(self):
        self.Create()

    def Create(self):
        print "New password"

c = Child()

p = Parent()

