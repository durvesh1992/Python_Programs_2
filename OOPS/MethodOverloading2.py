class Human(object):

    def say_hello(self, *args, **kwargs):

        if args:
            for names in args:
                print "Hello; ", names

        if kwargs:
            for cars in kwargs:
                print "Carname: ", kwargs[cars]

h1 = Human()
h1.say_hello()

# Sending args
h1.say_hello("Aditya", "Tanmay")

#Sending KwARGS
h1.say_hello("Aditya", "Tanmay", car = "DodgeCharger")