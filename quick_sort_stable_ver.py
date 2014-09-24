import random
from SortTester import compare

def quick_sort_stable_ver(data):
    if len(data) < 2:
        return data
    else:
        pivot = random.choice(data)

        smaller = quick_sort_stable_ver([x for x in data if compare(x, "<", pivot, 'tuple')])
        bigger = quick_sort_stable_ver([x for x in data if compare(x, ">=", pivot, 'tuple')])

        return smaller + [pivot] + bigger
   
