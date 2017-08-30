class Robot(object):
    # Clas varianble
    population = 0

    # will get initialized when an object of the class is created
    def __init__(self,name):
        self.name = name

        Robot.population += 1
        #this would create object specific population variable
        #self.population += 1

    def say_hi(self):
        print "greetings from {}".format(self.name)

    def die(self):
        Robot.population -= 1
        if Robot.population == 0:
            print "None alive"
        else:
            print "we have {:d} robot available".format(Robot.population)

    # constructor for class method
    @classmethod
    def how_many(cls):
        print "we have {:d} robot available".format(cls.population)




# create instance of the object
droid1 = Robot("r2-d2")

# call the class method
droid1.say_hi()

# Call the class variable
print droid1.population
print "using constructor and class method:",Robot.how_many()


# create instance of the object
droid2 = Robot("r3-d3")

# call the class method
droid2.say_hi()

# Call the class variable
print droid2.population
print "using constructor and class method:",Robot.how_many()


droid1.die()
droid2.die()
droid1.how_many()