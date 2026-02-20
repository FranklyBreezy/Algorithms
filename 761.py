class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 2:
            return s
        
        count = 0
        start = 0
        substrings = []
        
        for i, char in enumerate(s):
            if char == '1':
                count += 1
            else:
                count -= 1
            
            # Found a balanced special substring
            if count == 0:
                # Recursively process inner substring
                inner = self.makeLargestSpecial(s[start + 1:i])
                substrings.append('1' + inner + '0')
                start = i + 1
        
        # Sort in descending order to maximize lexicographically
        substrings.sort(reverse=True)
        
        return ''.join(substrings)