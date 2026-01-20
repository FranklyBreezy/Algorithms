class Solution(object):
    def minBitwiseArray(self, nums):
        ans = []
        
        for x in nums:
            # If x is even, impossible
            if x % 2 == 0:
                ans.append(-1)
                continue
            
            # If x is all 1s in binary (x & (x + 1) == 0)
            if (x & (x + 1)) == 0:
                ans.append(x >> 1)
                continue
            
            # Find lowest zero bit in x
            lowest_zero = (~x) & (x + 1)
            
            # Compute minimum ans[i]
            ans.append(x - (lowest_zero >> 1))
        
        return ans
