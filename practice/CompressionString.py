class CompressionString(object):

    def compression_string(self, x):
        print x
        i = 0
        length = len(x)
        compression_list = []
        while i < length:
            compression_list.append(x[i])
            count = 1

            while ((i+1) < length and x[i+1] == x[i]):
                count += 1
                i += 1

            if count > 1:
                compression_list.append(str(count))
            i += 1
        print ''.join(compression_list)


a="aaaabbbbbbbbbbbbbbccdddeabc"
c = CompressionString()
c.compression_string(a)

