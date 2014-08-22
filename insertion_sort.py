def insertion_sort(data):
    for i in range(1, len(data)):
        if data[i] < data[i - 1]:
            num = data.pop(i)

            for k in reversed(range(i - 1)):
                if (num != None) and (data[k] <= num):
                    data.insert(k + 1, num)
                    num = None
            
            if not num == None:
                data.insert(0, num)

    return data
