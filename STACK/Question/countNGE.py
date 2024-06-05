def merge(v, temp, low, mid, high):
    size1 = mid - low + 1
    size2 = high - mid

    a = v[low:mid+1]
    b = v[mid+1:high+1]

    i = 0
    j = 0
    k = low

    while i < size1 and j < size2:
        if a[i][0] < b[j][0]:
            temp[a[i][1]] += size2 - j
            v[k] = a[i]
            i += 1
        else:
            v[k] = b[j]
            j += 1
        k += 1

    while i < size1:
        v[k] = a[i]
        i += 1
        k += 1

    while j < size2:
        v[k] = b[j]
        j += 1
        k += 1


def mergeSort(v, temp, low, high):
    if low < high:
        mid = low + (high - low) // 2
        mergeSort(v, temp, low, mid)
        mergeSort(v, temp, mid + 1, high)
        merge(v, temp, low, mid, high)


def count_next_greater_elements(arr, query_indices):
    n = len(arr)
    temp = [0] * n
    v = [(arr[i], i) for i in range(n)]
    
    mergeSort(v, temp, 0, n - 1)
    
    result = [temp[j] for j in query_indices]
    
    return result


# Example usage
input_arr = [1, 3, 6, 5, 8, 9, 13, 4]
query_indices = [0, 1, 5]

output = count_next_greater_elements(input_arr, query_indices)
print(output)  # Output: [4, 4, 2]
