import time, random, sys

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
            print "Time of my work: ", time.clock() - begin
##            print self.data

try:
    sorter = getattr(__import__(sys.argv[1]), sys.argv[1])
except IndexError:
    print "Sorry, but you need to add sorting module which you are going to test as second argument"
    exit()
except ImportError:
    print "I can't find file to import. Maybe you wrote '.py' in the end, or you misspeled. Check yourself and try again!"
    exit()
except AttributeError:
    print "There is no attribute ", sys.argv[1], ". Try again."
    exit()

for i in [100, 250, 500, 750, 1000, 2500, 5000, 7500, 10000]:
    test = SortTester(i)
    print i, " elements in a list.",
    test.run(sorter)
