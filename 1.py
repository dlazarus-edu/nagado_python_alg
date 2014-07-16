import time,random

def sorter(l):
    for i in range(len(l) - 1):
        n1 = 0

        while (n1 + 1) < len(l):
            if l[n1] > l[n1+1]:
                l[n1], l[n1+1] = l[n1+1], l[n1]
            n1 += 1
        

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
            self.data.append(random.randrange(lmin,lmax,1))    


    def sort(self):
        sorter(self.data)


    def __str__(self):
        m = ''

        for i in self.data:
            m = m + str(i) + ' ' 

        return m


m = MyList(input("Enter length of list: "))
begin = time.clock()
m.sort()
end = time.clock()
print "List is sorted. Time of my work: ", time.clock() - begin
print m



