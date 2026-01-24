class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        max_sum = 0

        while left < right:
            max_sum = max(max_sum, nums[left] + nums[right])
            left += 1
            right -= 1

        return max_sum
