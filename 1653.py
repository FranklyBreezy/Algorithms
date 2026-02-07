class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        b_count = 0
        deletions = 0

        for ch in s:
            if ch == 'b':
                b_count += 1
            else:  # ch == 'a'
                deletions = min(deletions + 1, b_count)

        return deletions
