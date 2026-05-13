def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]   # choosing last element as pivot

    left = []
    right = []

    for i in arr[:-1]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)



numbers = [8, 3, 1, 7, 0, 10, 2]

sorted_numbers = quick_sort(numbers)

print("Sorted array:", sorted_numbers)