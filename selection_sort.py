def selection_sort(data):
    for k in range(len(data)):
        min = data[k]
        
        for i in range(k, len(data)):
              if data[i] < min:
                  min = data[i]
                  
        data.remove(min)
        data.insert(k, min)

    return data
