class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        dp = [[0.0] * 100 for _ in range(100)]
        dp[0][0] = float(poured)
        
        # Only simulate until the row before query_row
        for r in range(query_row):
            for c in range(r + 1):
                if dp[r][c] > 1.0:
                    overflow = (dp[r][c] - 1.0) / 2.0
                    dp[r][c] = 1.0
                    dp[r + 1][c] += overflow
                    dp[r + 1][c + 1] += overflow
        
        return min(1.0, dp[query_row][query_glass])
