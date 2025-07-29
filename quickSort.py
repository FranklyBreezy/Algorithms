def quickSort(arr,low,high):
    if low < high:
        pivotIndex = partition(arr,low,high)
        quickSort(arr,low,pivotIndex-1)
        quickSort(arr,pivotIndex+1,high)

def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range(low,high):
        if arr[j] < pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high], arr[i+1]
    return i+1

arr = [5, 2, 9, 1, 6]
(quickSort(arr, 0, len(arr) - 1))
print(arr)

# Time complexity: 
# Worst case: O(n^2)
# - Happens if the pivot chosen is always the smallest or largest element, 
#   causing one side to be empty and the other side to have n-1 elements.
# - This causes n levels of recursion, and at each level, you process up to n elements.
# Average case: O(n log n)
# - Usually, the pivot divides the list into roughly equal halves.
# - There are log n levels of recursion (splitting the list).
# - At each level, partitioning processes all n elements once.
# - Total Time = O(n log n)

# Space complexity: O(log n)
# - Because this is an in-place sort, no extra arrays are created.
# - The extra space comes from the recursion stack.
# - In the best and average cases, the recursion depth is about log n.
# - In the worst case (unbalanced splits), recursion depth can be n.
# - So typically O(log n) space, worst case O(n).
