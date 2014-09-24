import random
from SortTester import compare

def quick_sort(data):
    sort_worker(0, len(data) - 1, data)

    return data


def sort_worker(begin, end, data):
    if begin < end:
        k = begin
        k2 = end
        num = random.randrange(begin, end + 1, 1)
        if num > end:
            num = end
        num = data[num]
        isSmaller = False
        isBigger = False
        center = end - 1
        while k < k2:
            if compare(data[k], '<', num, 'tuple'):
                k += 1
            else:
                isBigger = True

            if compare(data[k2], '>=', num, 'tuple'):
                k2 -= 1
            else:
                isSmaller = True

            if isBigger == True and isSmaller == True:
                data[k], data[k2] = data[k2], data[k]
                isSmaller = False
                isBigger = False
                k += 1
                k2 -= 1

            if compare(data[k2], '>=', num, 'tuple'):
                center = k2
            else:
                center = k2 + 1


        if end - begin == 1:
            if compare(data[begin], '>', data[end], 'tuple'):
                data[begin], data[end] = data[end], data[begin]
        if [x for x in data[begin:end + 1] if compare(x, '!=', data[begin], 'tuple')] != [] and (end - begin > 1):
            sort_worker(begin, center - 1, data)
            sort_worker(center, end, data)

 
        
         
