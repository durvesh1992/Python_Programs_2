class Parent(object):
    pass

    def foo(self,x):
        print x


    @staticmethod
    def mystatic(x, y):
        print "hi"

    def notfoo(self, *args):
        print args
        self.foo(args)
        self.mystatic(args,args)

        Parent.mystatic(args, args)
        # not gonna work
#        Parent.foo(args)



p = Parent()
p.foo(1)
p.notfoo(2)

