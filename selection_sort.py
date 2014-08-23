from SortTester import compare

def selection_sort(data):
    for k in range(len(data)):
        minNum = data[k]
        
        for i in range(k, len(data)):
              if compare(data[i], '<', minNum, 'tuple'):
                  minNum = data[i]
                  
        data.remove(minNum)
        data.insert(k, minNum)

    return data
