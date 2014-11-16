from SortTester import compare

def merge_sort(data):
    if len(data) > 1:
        middle = int(len(data) / 2)

        left = merge_sort(data[:middle])
        right = merge_sort(data[middle:])

        data = merge(left,right)

    return data

        

def merge(list1, list2):
    merged_list = []

    while (len(list1) >= 1) and (len(list2) >= 1):
        if compare(list1[0], '<', list2[0], 'tuple'):
            merged_list.append(list1.pop(0))

        elif list1[0] == list2[0]:
            merged_list.append([list1.pop(0),list2.pop(0)])

        else:   
            merged_list.append(list2.pop(0))
   
    if len(list1) > 0: merged_list += list1
    if len(list2) > 0: merged_list += list2
  

    return merged_list

