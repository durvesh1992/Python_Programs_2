class Parent(object):

    __hiddenVariable = 0
    def add(self,x):
        self.__hiddenVariable +=x
        print self.__hiddenVariable

p = Parent()

p.add(2)
p.add(4)

# This next line would give an error
#p.__hiddenVariable
