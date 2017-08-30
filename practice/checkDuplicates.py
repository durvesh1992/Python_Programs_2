import itertools

class CheckDuplicate:
    def __init__(self, nums, *args, **kwargs):
        self.nums = nums.split(',')

        for arg in args:
            print arg

        print kwargs
        for key,val in kwargs.iteritems():
            print key, val


    def check_duplicates(self):
        self.numList = map(int, self.nums)
        duplist = []
        for number in self.numList:
            if number not in duplist:
                duplist.append(number)
            else:
                continue
        return duplist

    def print_val(self):
        print "Value obtained is: {}".format(map(int, self.nums))

class RemoveElement:

    def remove_element(self,a,unwanted_element):
        self.element = a
        m = 0

        for i in a:
            if i == unwanted_element:
                self.element.remove(i)

        print self.element
        print a

# Check Dup
nums = "4,3,2,7,8,2,3,1"
c = CheckDuplicate(nums, 'lilee', 'wma', 'zcc', barca='messi')
c.print_val()
print c.check_duplicates()

#remove element

a=[3,5,2,7,8,9,2]
b = 2
#RemoveElement.remove_element()
dup = RemoveElement()
dup.remove_element(a, b)
