def fibonacci_search(some_list, target):
    if target > some_list[-1]:
        return None

    size = len(some_list)

    fib_num_list = [0, 1, 2]
    while fib_num_list[-1] < size:
        fib_num_list.append(fib_num_list[-2] + fib_num_list[-1])

    j_reincarnations = []
    i = 0
    j = 0
    while True:
        current_el = some_list[min(j + fib_num_list[i], size-1)]

        if target == current_el:
            return min(j + fib_num_list[i], size-1)
        if target > current_el:
            i += 1
            continue
        if target < current_el:
            j = fib_num_list[i-1]
            i = 0
            if j in j_reincarnations:
                return None
            j_reincarnations.append(j)
            continue


def fibonacci_insert(some_list, x):
    copy_some_list = some_list.copy()
    if x > some_list[-1]:
        some_list.append(x)
        return some_list

    size = len(some_list)

    fib_num_list = [0, 1, 2]
    while fib_num_list[-1] < size:
        fib_num_list.append(fib_num_list[-2] + fib_num_list[-1])

    j_reincarnations = []
    i = 0
    while True:
        current_el = some_list[min(fib_num_list[i], size-1)]

        if x > current_el:
            i += 1
            # print(some_list)
            continue
        if x < current_el:
            j = fib_num_list[i-1]
            i = 0
            some_list[:] = some_list[j:]
            print(some_list)
            if j in j_reincarnations:
                resuls_list = copy_some_list[:size-len(some_list)]
                resuls_list.append(some_list[0])
                some_list.pop(0)
                resuls_list.append(x)
                resuls_list.extend(some_list)
                print("---------------")
                return resuls_list
            j_reincarnations.append(j)
            continue


def fibonacci_delete(some_list, x):
    if x > some_list[-1]:
        return None

    size = len(some_list)

    fib_num_list = [0, 1, 2]
    while fib_num_list[-1] < size:
        fib_num_list.append(fib_num_list[-2] + fib_num_list[-1])

    j_reincarnations = []
    i = 0
    j = 0
    while True:
        current_el = some_list[min(j + fib_num_list[i], size - 1)]

        if x == current_el:
            some_list.pop(min(j + fib_num_list[i], size - 1))
            return some_list
            return
        if x > current_el:
            i += 1
            continue
        if x < current_el:
            j = fib_num_list[i - 1]
            i = 0
            if j in j_reincarnations:
                return None
            j_reincarnations.append(j)
            continue


# some_list = [1, 0, 8, 9, 2, 2, 10, 11, 3, 4, 4, 4, 4, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 98, 100]
# some_list.sort()
# print(some_list)

# smth_to_find = int(input())
# print(fibonacci_search(some_list, smth_to_find))

#print(fibonacci_insert(some_list, 25))

# print(fibonacci_delete(some_list, 24))