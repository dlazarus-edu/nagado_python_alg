# test
import time
from random import randrange

def sorter(l):
    n1 = 0
    n2 = 1

    while n1 < len(l) and n2 < len(l):
        if l[n1] > l[n2]:
            k = l[n1]
            l[n1] = l[n2]
            l[n2] = k
        n1 += 1
        n2 += 1

    return l
        

def check(l):
    for i in range(len(l)-1):
        if l[i] > l[i + 1]:
            return True
            break

    return False

class MyList:

    def __init__(self, length, lmax = 13579, lmin = 0):
        self.data = []
   
        for i in range(length):
            self.data.append(randrange(lmin,lmax,1))    


    def sort(self):
        while check(self.data):
            self.data = sorter(self.data)


    def __str__(self):
        m = ''

        for i in self.data:
            m = m + str(i) + ' ' 

        return m

begin = time.clock()
m = MyList(input("Enter length of list: "))
m.sort()
print "List sorted. Time of my work: ", time.clock() - begin


