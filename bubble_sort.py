def bubble_sort(data):
    for _ in range(len(data) - 1):
        n1 = 0
        counter = False
        while (n1 + 1) < len(data):
            if data[n1] > data[n1+1]:
                data[n1], data[n1+1] = data[n1+1], data[n1]
                counter = True
            n1 += 1

        if counter == False:
            break
        
    return data



