import random
import BS
import BTree
import FS

def massGenerator(n=50, min_limit=-250, max_limit=1013):
    a = [random.randint(min_limit, max_limit) for i in range(n)]
    print(a)
    return a






some_list = massGenerator(10, 0, 9)
#k = int(input())
#print(BS.binarySearch(some_list, k))
#BTree.heapify(some_list)
FS