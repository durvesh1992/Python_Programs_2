class SchoolMember(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print "initialized school member {}".format(self.name)

    def tell(self):
        print ("Name: {}, Age: {:d}".format(self.name, self.age))
        print "phirse aya"


class Teacher(SchoolMember):
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print "Initialized teacher: {}".format(self.name)
    def tell(self):
        SchoolMember.tell(self)
        print "salary: {}".format(self.salary)

        print "going to super parent"
        super(Teacher,self).tell()

class Student(SchoolMember):
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print "Initialized Student: {}".format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print "Marks: {}".format(self.marks)

t = Teacher("ram",20,800)
s = Student("shyam", 10, 99)

members = [t,s]
for member in members:
    member.tell()

