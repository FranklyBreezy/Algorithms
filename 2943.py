class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        """
        :type n: int
        :type m: int
        :type hBars: List[int]
        :type vBars: List[int]
        :rtype: int
        """

        def longest_consecutive(arr):
            arr.sort()
            longest = curr = 1
            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] + 1:
                    curr += 1
                    longest = max(longest, curr)
                else:
                    curr = 1
            return longest

        max_h = longest_consecutive(hBars)
        max_v = longest_consecutive(vBars)

        side = min(max_h + 1, max_v + 1)
        return side * side
