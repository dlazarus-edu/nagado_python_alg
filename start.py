import sys, SortTester

if len(sys.argv) == 2:
    name = sys.argv[1]
else:
    print "You need to enter name of program that you want to test"
    exit()

try: 
    sorter = getattr(__import__(name), name)
except ImportError:
    print "I can't find file to import. Maybe you wrote '.py' in the end, or you misspeled. Check yourself and try again!"
    exit()
except AttributeError:
    print "There is no attribute ", name, ". Try again."
    exit()

for i in [100, 250, 500, 750, 1000, 2500, 5000, 7500, 10000]:
    test = SortTester.SortTester(i)
    print i, "elements in a list.",
    test.run(sorter)
