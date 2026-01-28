import heapq
import bisect

class Solution(object):
    def minCost(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        INF = float('inf')

        # dist[i][j][t] = min cost to reach (i, j) using t teleports
        dist = [[[INF] * (k + 1) for _ in range(n)] for _ in range(m)]
        dist[0][0][0] = 0

        # Preprocess cells sorted by value
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j], i, j))
        cells.sort()  # sort by grid value
        values = [c[0] for c in cells]

        pq = [(0, 0, 0, 0)]  # (cost, i, j, teleports_used)

        while pq:
            cost, i, j, t = heapq.heappop(pq)

            if cost > dist[i][j][t]:
                continue

            # If we reached destination, we can early exit
            if i == m - 1 and j == n - 1:
                return cost

            # Normal moves: right and down
            for ni, nj in ((i + 1, j), (i, j + 1)):
                if 0 <= ni < m and 0 <= nj < n:
                    new_cost = cost + grid[ni][nj]
                    if new_cost < dist[ni][nj][t]:
                        dist[ni][nj][t] = new_cost
                        heapq.heappush(pq, (new_cost, ni, nj, t))

            # Teleportation
            if t < k:
                # All cells with value <= grid[i][j]
                limit = grid[i][j]
                idx = bisect.bisect_right(values, limit)

                for _, x, y in cells[:idx]:
                    if cost < dist[x][y][t + 1]:
                        dist[x][y][t + 1] = cost
                        heapq.heappush(pq, (cost, x, y, t + 1))

        # Final answer: min cost to reach destination with ≤ k teleports
        return min(dist[m - 1][n - 1])
