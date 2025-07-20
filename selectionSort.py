#def selectionSort(arr):
#    for i in range(len(arr)):
#        for j in range(i,len(arr)):
#            if arr[i] > arr[j]:
#                arr[i], arr[j] = arr[j], arr[i]
#    return arr

def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[min]>arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr
arr = list(map(int,input().split()))
print(selectionSort(arr))