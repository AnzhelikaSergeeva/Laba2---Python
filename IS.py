def interpolation_search(some_list, target):
    some_list.sort()
    print(some_list)
    left = 0
    right = len(some_list) - 1
    while left <= right and some_list[left] <= target <= some_list[right]:

        d = left + int(((float(right - left) / (some_list[right] - some_list[left])) * (target - some_list[left])))

        if some_list[d] == target:
            return d
        elif target < some_list[d]:
            right = d - 1
        elif target > some_list[d]:
            left = d + 1
    return -1


def interpolation_insert(some_list, target):
    some_list.sort()
    print(some_list)
    left = 0
    right = len(some_list) - 1
    while left <= right and some_list[left] <= target <= some_list[right]:

        d = left + int(((float(right - left) / (some_list[right] - some_list[left])) * (target - some_list[left])))

        if some_list[d] == target:
            break
        elif target < some_list[d]:
            right = d - 1
        elif target > some_list[d]:
            left = d + 1

    result_list = some_list[:d + 1]
    result_list.append(target)
    result_list += some_list[d + 1:]
    return result_list


def interpolation_delete(some_list, target):
    interpolation_search(some_list, target)
    del some_list[target]




some_list = [1, 0, 8, 9, 2, 2, 10, 11, 3, 4, 4, 4, 4, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 98, 100]

smth_to_find = int(input())
#print(interpolation_search(some_list, smth_to_find))
print(interpolation_insert(some_list, 1))