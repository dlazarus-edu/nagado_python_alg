import time, random, sys

class SortTester:
    def __init__(self, length, key = 'random', lmax = 13579, lmin = 0):
        self.data = []
        
        if key == 'random':
            for _ in range(length):
                num = random.randrange(0, 999999999, 1) ##Try do-while
                while num in self.data: 
                    num = random.randrange(0, 999999999, 1)
                self.data.append(num)    
        elif key == 'sorted':
            for i in range(length):
                self.data.append(i)
        elif key == 'reverse_sorted':
            for i in range(length):
                self.data.append(length-i)
        elif key == 'random_doubled':
            while len(self.data) < length:
                repeats = random.randrange(1, 5, 1)
                for _ in range(repeats):
                    if len(self.data) < length:
                        self.data.append(random.randrange(0, 999999999, 1))


    def check(self):
        for i in range(len(self.data)-1):
            if self.data[i] > self.data[i + 1]:
                return True

        return False

    def simple_test(self, sort_func):
        sort_func(self.data)

        if self.check():
            print("Something is wrong")
        else:
            print("Well done!")

    def run(self, sort_func):
        begin = time.clock()
        sort_func(self.data)
        end = time.clock()

        if self.check():
            print("Something is wrong")
        else:
            print ("Time of my work: ", time.clock() - begin)
##            print(self.data)

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
