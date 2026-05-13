def merge(array_a, array_b):
    merged = []
    i, j = 0, 0
    while i < len(array_a) and j < len(array_b):
        if array_a[i] < array_b[j]:
            merged.append(array_a[i])
            i += 1
        else: 
            merged.append(array_b[j])
            j += 1
    merged.extend(array_a[i:])
    merged.extend(array_b[j:])
    return merged
a=merge([1, 3, 5], [2, 4, 6])
print(a)