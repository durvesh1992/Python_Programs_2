def say_hello(x):

    x += "dec"
    print x

def changme(y):
    y[len(y) - 1] = 0
    print y

x = "abc"
print x
say_hello(x)
print x

y = [1,2,3]
changme(y)
print y
