class Human(object):

    def say_hello(self, name= None):
        if name != None:
            print "Hello", name
        else:
            print "You should get a name for yourself"

    # Output goes only into the second function...why ???
    def say_hello(self, *args):
        print "I am in second function"

h1 = Human()
h1.say_hello()

# User getting a name for itself
h1.say_hello("Aditya")
