import sys

class BinarySearch(object):
    def __init__(self,num,search, first, middle, last):
        self.number = num
        self.search = search
        self.first = first
        self.last = last
        self.middle = middle

    def binary_search(self, num, search, first, last, middle):
        #while self.first <= self.last:

        print num

        while first <= last:
            print first, last, middle, search
            if num[middle] < search:
                first = middle + 1
            elif num[middle] == search:
                print "found"
                sys.exit()
            else:
                last = middle - 1
            middle = (first + last) / 2
        if first > last:
            print "Not found"


num = [1,2,3,4,5,6,7,8,899]
search = 8
first = 0
last = len(num) - 1
middle = (first + last) / 2

print first, last, middle, search
b = BinarySearch(num, search, first, last, middle)
b.binary_search(num, search, first, last, middle)