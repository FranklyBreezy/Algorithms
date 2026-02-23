class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        n = len(s)
        
        # If total possible substrings is greater than what s can provide
        if n < k:
            return False
        
        needed = 1 << k  # 2^k
        seen = set()
        
        for i in range(n - k + 1):
            substring = s[i:i+k]
            seen.add(substring)
            
            # Early stop if we've found all possibilities
            if len(seen) == needed:
                return True
        
        return len(seen) == needed