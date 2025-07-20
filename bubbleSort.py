def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
#complexity is 0(n^2) as there are 2 loops, one outer loop and one inner loop.

# Example
print(bubbleSort([64, 34, 25, 12, 22, 11, 90]))

arr = list(map(int,input().split()))
print(bubbleSort(arr))