def binary_Search(mass, element):
    mass.sort()
    print(mass)
    left = 0
    right = len(mass) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if (element == mass[middle]):
            return middle
        elif (element < mass[middle]):
            right = middle - 1
        elif (element > mass[middle]):
            left = middle + 1
    return -1


def binary_insert(mass, element):
    mass.sort()
    print(mass)
    left = 0
    right = len(mass) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if (element == mass[middle]):
            break
        elif (element < mass[middle]):
            right = middle - 1
        elif (element > mass[middle]):
            left = middle + 1

    result = mass[:middle]
    result.append(element)
    result += mass[middle:]
    return result


def binary_delete(mass, element):
    del mass[binary_Search(mass, element)]
    return mass


some_list = [8, 0, 3, 1, 5, 3, 5, 3, 5, 8]
#print(binary_Search(some_list, 8))
# print(binary_insert(some_list, 5))
print(binary_delete(some_list, 8))