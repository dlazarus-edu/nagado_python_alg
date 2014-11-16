import time, random

class SortTester:
    def __init__(self, length, key = 'random', lmax = 13579, lmin = 0):
        self.data = []
        
        if key == 'random':
            for i in range(length):
                num = str(random.randrange(0, 999999999, 1))
                while num in self.data: 
                    num = str(random.randrange(0, 999999999, 1))                    
                self.data.append((i, num))    
        elif key == 'sorted':
            for i in range(length):
                self.data.append((i, str(i)))
        elif key == 'reverse_sorted':
            for i in range(length):
                self.data.append((i, str(length-i)))
        elif key == 'random_doubled':
            while len(self.data) < length:
                repeats = random.randrange(1, 5, 1)
                for _ in range(repeats):
                    if len(self.data) < length:
                        self.data.append((len(self.data), str(random.randrange(0, 999999999, 1))))
        elif key == 'same':
            for i in range(length - 1):
                if i % 2 == 0:
                    self.data.append((i, 3))
                else:
                    self.data.append((i,5))
          
    def check(self):
        for i in range(len(self.data)-1):
            if compare(self.data[i], '>', self.data[i + 1], 'tuple'):
                return True

        return False

    def checkOrder(self):
        k = False

        for i in range(len(self.data) - 1):
            if compare(self.data[i], '==', self.data[i + 1], 'tuple'):
                if compare(self.data[i], '>', self.data[i + 1], 'tuple', 0):
                    k = True

        if k == True:
            print("not stable")
        else:
            print("stable")

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

    def printMe(self):
        for i in self.data:
            print(i, end=" ")

        print()


def compare(el1, sign, el2, mode = 'usual', num = 1):
    if mode == 'usual':
        if sign == '>' and el1 > el2:
            return True
        if sign == '==' and el1 == el2:
            return True
        if sign == '<' and el1 < el2:
            return True
        if sign == '!=' and el1 != el2:
            return True
        if (sign == '>=' or sign == '=>') and el1 >= el2:
            return True
        if (sign == '<=' or sign == '=<') and el1 <= el2:
            return True

    elif mode == 'tuple':
        if sign == '>' and el1[num] > el2[num]:
            return True
        if sign == '==' and el1[num] == el2[num]:
            return True
        if sign == '<' and el1[num] < el2[num]:
            return True
        if sign == '!=' and el1[num] != el2[num]:
            return True
        if (sign == '>=' or sign == '=>') and el1[num] >= el2[num]:
            return True
        if (sign == '<=' or sign == '=<') and el1[num] <= el2[num]:
            return True


    return False
    
