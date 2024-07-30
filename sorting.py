import random
import time


def radix_sort(arr):
    frq = [[] for _ in range(10)]
    maximum = max(arr)
    i = 1
    while i < maximum:
        while len(arr) > 0:
            frq[(arr[0] // i) % 10].append(arr.pop(0))
        for f in frq:
            while len(f) > 0:
                arr.append(f.pop(0))
        i *= 10
    return arr


def counting_sort(arr, minimum=None, maximum=None):
    if minimum is None:
        minimum = min(arr)
    if maximum is None:
        maximum = max(arr)
    frq = [0 for _ in range(maximum - minimum + 1)]
    for item in arr:
        frq[item - minimum] += 1

    result = []
    for i, f in enumerate(frq):
        while f > 0:
            result.append(i + minimum)
            f -= 1

    return result


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        i = len(arr) // 2
        l = merge_sort(arr[:i])
        r = merge_sort(arr[i:])
        s_arr = []
        while len(l) > 0 and len(r) > 0:
            if l[0] < r[0]:
                s_arr.append(l.pop(0))
            else:
                s_arr.append(r.pop(0))
        while len(l) > 0:
            s_arr.append(l.pop(0))
        while len(r) > 0:
            s_arr.append(r.pop(0))
        return s_arr


def bubble_sort(arr):
    i = 0
    j = len(arr)
    swaped = False
    while j > 1:
        while i < j - 1:
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaped = True
            i += 1
        if not swaped:
            break
        swaped = False
        j -= 1
        i = 0
    return arr


def insertion_sort(arr):
    sorted_arr = []
    number = len(arr)
    while len(sorted_arr) < number:
        item = arr.pop(0)
        index = len(sorted_arr)
        while index > 0 and item < sorted_arr[index - 1]:
            index -= 1
        sorted_arr.insert(index, item)
    return sorted_arr


def selection_sort(arr):
    i = 0
    while i < len(arr):
        minimum = arr[i]
        minimum_index = i
        for j, item in enumerate(arr[i + 1:]):
            if item < minimum:
                minimum = item
                minimum_index = j + i + 1
        arr[i], arr[minimum_index] = arr[minimum_index], arr[i]
        i += 1
    return arr


if __name__ == "__main__":
    number = 20
    arr = [random.randint(0, 2000) for _ in range(number)]
    print(f"unsorted array: {arr} ")
    start_time = time.time()
    arr = radix_sort(arr)
    print(f"sorted array: {arr} ")
    print(f"duration: {time.time() - start_time}")
    arr = [i for i in range(number, 0, -1)]
    print(f"unsorted array: {arr} ")
    start_time = time.time()
    arr = bubble_sort(arr)
    print(f"sorted array: {arr} ")
    print(f"duration: {time.time() - start_time}")
