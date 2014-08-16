import time, random

class SortTester:
    def __init__(self, length, key = 'random', lmax = 13579, lmin = 0):
        self.data = []
        
        if key == 'random':
            for _ in range(length):
                num = random.randrange(0, 999999999, 1)
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
        self.data = sort_func(self.data)

        if self.check():
            print("Something is wrong")
        else:
            print("Well done!")

    def run(self, sort_func):
        begin = time.clock()
        self.data = sort_func(self.data)
        end = time.clock()

        if self.check():
            print("Something is wrong")
        else:
            print(round(time.clock() - begin, 7), end=" ")

    def __str__(self):
        for i in self.data:
            print(i, end=" ")
    
        return ""
