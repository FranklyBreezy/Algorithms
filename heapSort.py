def heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    
    # Build a maxheap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements one by one
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr

# Example
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Heap Sort:", arr)
# Time complexity:
# - Building the max heap takes O(n) time.
# - Extracting elements one by one and heapifying takes O(log n) per element.
# - Total time complexity is O(n log n) for all cases (best, average, worst).

# Space complexity: O(1)
# - Heap sort sorts the array in place.
# - Uses only a constant amount of extra memory.