from SortTester import compare

def insertion_sort(data):
    for i in range(1, len(data)):
        if compare(data[i], '<', data[i - 1], 'tuple'):
            num = data.pop(i)

            for k in reversed(range(i - 1)):
                if (num != None) and (compare(data[k], '<=', num, 'tuple')):
                    data.insert(k + 1, num)
                    num = None
            
            if not num == None:
                data.insert(0, num)

    return data
