def bubble_sort(data):
    for _ in range(len(data) - 1):
        n1 = 0
      ##  counter = 0
        while (n1 + 1) < len(data):
            if data[n1] > data[n1+1]:
                data[n1], data[n1+1] = data[n1+1], data[n1]
 ##               counter += 1
            n1 += 1

       ## if counter == 0:
          ##  break
        



