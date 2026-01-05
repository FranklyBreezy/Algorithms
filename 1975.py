class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        total = 0
        neg_count = 0
        min_abs = float('inf')

        for row in matrix:
            for x in row:
                total += abs(x)
                if x < 0:
                    neg_count += 1
                min_abs = min(min_abs, abs(x))

        if neg_count % 2 == 0:
            return total
        else:
            return total - 2 * min_abs
