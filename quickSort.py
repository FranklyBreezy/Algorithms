def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    
    return quick_sort(less) + [pivot] + quick_sort(greater)

# Example
arr = [10, 7, 8, 9, 1, 5]
print("Quick Sort:", quick_sort(arr))
