class MaxWord(object):

    def __init__(self,x):
        self.x = x

    def max_word(self):
        d = {}
        maxlist = []
        mylist = self.x.split(' ')
        for i in mylist:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        # will return max key value
        maximum = max(d, key = d.get)

        print "Maximum Value obtained: ", d[maximum]

        # to find the max value if
        for i in d:
            if d[i] == d[maximum]:
                maxlist.append(i)

        return  maxlist
c = 'durvesh pilankar aditi shah aditi shah'
cobj = MaxWord(c)
print cobj.max_word()

