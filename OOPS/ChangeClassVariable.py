class ECE(object):
    branch = "ece"
    pass

a = ECE()
b = ECE()

# initially

print a.branch
print b.branch

# Later
a.branch = "cmpe"
print a.branch
print b.branch

# Further
ECE.branch = "engineering"
print a.branch
print b.branch