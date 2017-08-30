class DeCompressionString(object):

    def decompression_string(self, x):

        numbers = "1234567890"
        i = 0
        length = len(x)
        decompression_list = []


        while i < length:

            if x[i].isalpha():
                decompression_list.append(x[i])

                character = x[i]
                my_num = ""

                while ((i+1) < length and x[i+1] in numbers):
                    my_num += x[i+1]
                    i += 1

                if my_num != "":
                    print "Value mila", my_num


                    for j in range(int(my_num)):
                        print j
                        if j == 0:
                            continue
                        decompression_list.append(character)

            i += 1
            print "My list->",decompression_list

a="a4b14c2d3eabc"
c = DeCompressionString()
c.decompression_string(a)

