class Solution(object):
    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        # Compute prefix sums
        rowSum = [[0]*n for _ in range(m)]
        colSum = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                rowSum[i][j] = grid[i][j] + (rowSum[i][j-1] if j>0 else 0)
                colSum[i][j] = grid[i][j] + (colSum[i-1][j] if i>0 else 0)
        
        def getRowSum(i, j1, j2):
            return rowSum[i][j2] - (rowSum[i][j1-1] if j1>0 else 0)
        
        def getColSum(j, i1, i2):
            return colSum[i2][j] - (colSum[i1-1][j] if i1>0 else 0)
        
        # Check if square at (i, j) with size k is magic
        def isMagic(i, j, k):
            target = getRowSum(i, j, j+k-1)
            # Check all rows
            for r in range(i, i+k):
                if getRowSum(r, j, j+k-1) != target:
                    return False
            # Check all columns
            for c in range(j, j+k):
                if getColSum(c, i, i+k-1) != target:
                    return False
            # Check main diagonal
            diag1 = sum(grid[i+x][j+x] for x in range(k))
            if diag1 != target:
                return False
            # Check anti-diagonal
            diag2 = sum(grid[i+x][j+k-1-x] for x in range(k))
            if diag2 != target:
                return False
            return True
        
        # Try sizes from largest to smallest
        for k in range(min(m,n), 0, -1):
            for i in range(m-k+1):
                for j in range(n-k+1):
                    if isMagic(i, j, k):
                        return k
        return 1  # at least 1x1 is magic
