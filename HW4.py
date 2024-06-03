import timeit
import random
import pandas as pd

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def timsort(arr):
    min_run = 32
    n = len(arr)
    
    for i in range(0, n, min_run):
        insertion_sort(arr[i:i + min_run])
    
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = min(n, start + size - 1)
            end = min(n, start + size * 2 - 1)
            merged = merge(arr[start:mid + 1], arr[mid + 1:end + 1])
            arr[start:start + len(merged)] = merged
        size *= 2

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

data_sizes = [1000, 5000, 10000]
test_data = {size: [random.randint(0, 100000) for _ in range(size)] for size in data_sizes}

results = {}
for size, data in test_data.items():
    results[size] = {
        'merge_sort': timeit.timeit(lambda: merge_sort(data.copy()), number=1),
        'insertion_sort': timeit.timeit(lambda: insertion_sort(data.copy()), number=1),
        'timsort': timeit.timeit(lambda: timsort(data.copy()), number=1),
        'builtin_sorted': timeit.timeit(lambda: sorted(data.copy()), number=1),
    }

results_df = pd.DataFrame(results).T
print(results_df)
