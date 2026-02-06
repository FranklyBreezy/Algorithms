class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)

        left = 0
        max_kept = 1  # at least one element is always balanced

        for right in range(n):
            while nums[right] > nums[left] * k:
                left += 1
            max_kept = max(max_kept, right - left + 1)

        return n - max_kept
