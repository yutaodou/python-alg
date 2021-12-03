from typing import List, Tuple


def bubble_sort(input: List[int]) -> List[int]:
    temp = None
    for i in reversed(range(len(input))):
        for j in range(i):
            if j + 1 >= len(input):
                continue

            if input[j] > input[j + 1]:
                temp = input[j + 1]
                input[j + 1] = input[j]
                input[j] = temp
    return input


def selection_sort(input: List[int]) -> List[int]:
    temp = None
    for i in range(len(input)):
        for j in range(i, len(input)):
            if input[j] < input[i]:
                temp = input[j]
                input[j] = input[i]
                input[i] = temp

    return input


def insertion_sort(input: List[int]) -> List[int]:
    res = []
    for value in input:
        if not res or value >= res[-1]:
            res.append(value)
        else:
            for i in reversed(range(len(res))):
                if res[i] < value:
                    res.insert(i + 1, value)
                    break
            else:
                res.insert(0, value)
    return res


def quick_sort(input: List[int]) -> List[int]:
    def sort(start: int, end: int):
        if start >= end:
            return

        middle = input[end]
        left = 0
        right = end - 1

        def swap(left, right):
            temp = input[left]
            input[left] = input[right]
            input[right] = temp

        while left < right:
            if input[left] <= middle:
                left += 1
            elif input[right] >= middle:
                right -= 1
            else:
                swap(left, right)

        if input[left] >= middle:
            swap(left, end)

        sort(0, left - 1)
        sort(left + 1, end)

    sort(0, len(input) - 1)
    return input


def merge_sort(input: List[int]) -> List[int]:
    if len(input) < 2:
        return input

    l = 0
    h = len(input)
    m = (h + l) // 2

    left = merge_sort(input[l:m])
    right = merge_sort(input[m:h])

    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        lv = left[i]
        rv = right[j]

        if rv >= lv:
            res.append(lv)
            i += 1
        else:
            res.append(rv)
            j += 1

    if i < len(left):
        res.extend(left[i:])

    if j < len(right):
        res.extend(right[j:])

    return res


if __name__ == "__main__":
    a = [11, 22, 2, 6, 4, 5, 3, 465, 3245, 1, 23, 123, 223]
    # print(selection_sort(a))
    # print(bubble_sort(a))
    # print(insertion_sort(a))
    # print(merge_sort(a))
    # print(quick_sort(a))
    print(quick_sort(a))
