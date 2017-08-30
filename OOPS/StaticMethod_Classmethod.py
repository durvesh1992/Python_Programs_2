class A(object):
    def foo(self,x):
        print "Values passed are %s %s"%(self, x)

    @classmethod
    def class_foo(cls, x):
        print "Values passed are %s %s" %(cls, x)

    @staticmethod
    def static_foo(x):
        print "Values passed are %s " %(x)

class Child(A):

    def call_parent(self):
        super(Child,self).foo(99)
a = A()

# Call to a method in class needs an instance of the class
a.foo(1)

#throws an error
#A.foo(1)


# Call Class method
a.class_foo(2)
A.class_foo(2)

print ""
# Call Static method can be done by the object or the class

a.static_foo(3)
A.static_foo(3)

print "Creating object b"
b = Child()
b.call_parent()