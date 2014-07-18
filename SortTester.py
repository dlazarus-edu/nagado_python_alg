import time, random

class SortTester:
    def __init__(self, length, lmax = 13579, lmin = 0):
        self.data = []
   
        for i in range(length):
            self.data.append(random.randrange(lmin, lmax, 1))    

    def check(self):
        for i in range(len(self.data)-1):
            if self.data[i] > self.data[i + 1]:
                return True

        return False

    def run(self, sort_func):
        begin = time.clock()
        sort_func(self.data)
        end = time.clock()

        if self.check():
            print "Something is wrong"
        else:
            print "List is sorted. Time of my work: ", time.clock() - begin
##            print self.data


