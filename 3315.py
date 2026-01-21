class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for num in nums:
            # Special case: no solution for 2
            if num == 2:
                ans.append(-1)
                continue

            # Find the highest bit of the last continuous block of 1s
            mask = 1
            while num & mask:
                mask <<= 1

            # Remove that leading 1
            ans.append(num - (mask >> 1))

        return ans
