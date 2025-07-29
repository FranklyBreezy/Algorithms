def mergeSort(arr):
    if len(arr)<=1:
        return arr
    
    mid = len(arr)//2
    left_half = mergeSort(arr[:mid])
    right_half = mergeSort(arr[mid:])    
    return merge(left_half,right_half)

def merge(left, right):
    result = []
    j = 0
    i = 0
    while i < len(left) and j < len(right):
        if left[i] < right [j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [11,2,8,7,4,5,6]
print(mergeSort(arr))

# Time complexity: O(n log n)
# Divide the list into halves (this takes log n steps, because you split in half again and again).
# Merge all the pieces back together (this takes O(n) time per level because you look at every item once while merging).
# Total Time = O(n log n)
# You do log n levels of splitting.
# At each level, you process all n elements while merging.

# Space complexity: O(n)
# Merge sort uses extra space to hold temporary subarrays during the merge step.
# At each level of recursion, temporary arrays store parts of the list.
# The total extra space used across all levels is proportional to the input size.
# So, even though you split recursively, you never need more than O(n) extra space overall.
