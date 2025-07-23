def max_subarray(arr, k):
    n = len(arr)
    if n < k:
        return "Length of subarray is greater than length of array."
    window_sum = sum(arr[:k])
    max_sum = window_sum
    st = 0
    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        if window_sum > max_sum:
            max_sum = window_sum
            st = i - k + 1
    return max_sum, arr[st:st + k]

arr = [7, 2, 5, 4, 3, 9, 12, 1]
k = 3
print(max_subarray(arr, k))
