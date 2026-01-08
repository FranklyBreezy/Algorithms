class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        
        # Initialize DP with very small numbers
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
        
        # Fill DP table bottom-up
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                product = nums1[i] * nums2[j]
                
                dp[i][j] = max(
                    product + max(0, dp[i + 1][j + 1]),  # take both
                    dp[i + 1][j],                         # skip nums1[i]
                    dp[i][j + 1]                          # skip nums2[j]
                )
        
        return dp[0][0]
