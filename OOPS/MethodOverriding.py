# Method overriding is runtime polymorphism

class Parent(object):

    my_class_var = "Lilee"

    def __init__(self):
        self.value = 1
#    value = 1

    def get_value(self):
        print "-> ",self.value
        my_method_var = "Yen"

    @staticmethod
    def my_static():
        print "haha I am static and i dont need anyone" \
              "yes !!!!"
class Child(Parent):


    def get_value(self):
        print "--->>", self.value + 1
        print "going to parent for more"

        super(Child, self).get_value()
        print "back to child"

        # Checking if methods can be called from class without instance
        #Parent.get_value() # this fails
        Parent.my_static() # this passes

        # Calling class variables
        print Parent.my_class_var
        print super(Child, self).my_class_var
        # Calling class variables
#        print Parent.my_method_var # throws an error

p = Parent()
p.get_value()

c = Child()
c.get_value()


