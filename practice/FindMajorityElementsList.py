class FindMajority(object):

    def find_majority_element(self, c):
        self.c = c
        count = self.count_elements()

        # parse through the new list
        maxi =  count[0]

        for i in self.c:
            if count[ord(str(i))] > maxi:
                maxi = count[ord(str(i))]
                number = i
            else:
                continue
        print "Maximum element is: ",maxi, number


    def count_elements(self):
        count = [0] * 256
        for i in self.c:
            print i
            count[ord(str(i))] += 1
        return count

c = [2,3,4,5,6,6]
myobj = FindMajority()
myobj.find_majority_element(c)
