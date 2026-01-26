class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        min_diff = float('inf')
        res = []

        # First pass: find minimum difference
        for i in range(len(arr) - 1):
            min_diff = min(min_diff, arr[i + 1] - arr[i])

        # Second pass: collect pairs with that difference
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == min_diff:
                res.append([arr[i], arr[i + 1]])

        return res
