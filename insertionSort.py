def insertionSort(arr):
    for i in range(len(arr)):
        for j in range(i,0,-1):
            if arr[j-1]>arr[j]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
            else:
                break
    return arr

arr = list(map(int,input().split()))
print(insertionSort(arr))
