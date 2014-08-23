import sys, SortTester, re


def test():
    testList = SortTester.SortTester(100)
    testList.simple_test(sorter)


def benchmark():
    for i in [100, 1000, 10000]:
        testList = SortTester.SortTester(i)
        testList.run(sorter)

    for key in ('sorted', 'reverse_sorted', 'random_doubled'):
        testList = SortTester.SortTester(10000, key)
        testList.run(sorter)

    print()


def work_on_arguments():
    global name, arg
    if len(sys.argv) == 3:
        name = sys.argv[1]
        arg = sys.argv[2]
        if '.py' in name:
            name = re.sub('.py', '', name)

    else:
        print("You need to enter name of program that you want to test or type of test(test or benchmark)")
        exit()


def get_sorter():
    try: 
        sorter = getattr(__import__(name), name)

    except ImportError:
        print("I can't find file to import. Check yourself and try again!")
        exit()

    except AttributeError:
        print("There is no attribute ", name, ". Try again.")
        exit()

    return sorter


work_on_arguments()
sorter = get_sorter()
if arg == 'test':
    test()

elif arg == 'benchmark':
    benchmark()

else:
   print('You need to give 2nd argument "test" or "benchmark".')
