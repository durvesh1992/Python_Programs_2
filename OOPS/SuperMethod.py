class Parent(object):
    def __init__(self):
        self.Create()

    def Create(self):
        print "Super Parent method"

class Child(Parent):

    def __init__(self):
        self.Create()

    def Create(self):
        print "Super Child"
        # Calling Parent method from Child
        super(Child, self).Create()

p = Parent()
c =  Child()
#c.Create()