class Bubblesort(object):

    def sorted(self, num):
        for i in range(len(num)):
            for j in range(len(num)- 1 -i):
                if num[i] > num[j]:
                    temp = num[i]
                    num[i] = num[j]
                    num[j] = temp

        print num
num = [88,55,66,99,22,1,4]
c = Bubblesort()
c.sorted(num)