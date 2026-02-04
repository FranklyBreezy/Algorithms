class Solution(object):
    def isTrionic(self, nums):
        n = len(nums)
        i = 0

        # 1) strictly increasing (must have at least one step)
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == 0:
            return False  # no initial increasing segment

        # 2) strictly decreasing (must have at least one step)
        j = i
        while j + 1 < n and nums[j] > nums[j + 1]:
            j += 1
        if j == i:
            return False  # no decreasing segment

        # 3) strictly increasing (must have at least one step)
        k = j
        while k + 1 < n and nums[k] < nums[k + 1]:
            k += 1
        if k == j:
            return False  # no final increasing segment

        # must use the whole array
        return k == n - 1
