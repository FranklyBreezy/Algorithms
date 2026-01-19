class Solution(object):
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])

        # Build prefix sum
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                ps[i + 1][j + 1] = (
                    ps[i][j + 1] +
                    ps[i + 1][j] -
                    ps[i][j] +
                    mat[i][j]
                )

        # Helper to check if a square of size k is possible
        def can(k):
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    total = (
                        ps[i][j]
                        - ps[i - k][j]
                        - ps[i][j - k]
                        + ps[i - k][j - k]
                    )
                    if total <= threshold:
                        return True
            return False

        # Binary search on side length
        left, right = 0, min(m, n)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
