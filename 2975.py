class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        MOD = 10**9 + 7

        # Add the boundary fences
        h = [1] + hFences + [m]
        v = [1] + vFences + [n]

        h.sort()
        v.sort()

        # Compute all possible horizontal distances
        h_dist = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                h_dist.add(h[j] - h[i])

        # Compute all possible vertical distances
        v_dist = set()
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                v_dist.add(v[j] - v[i])

        # Find the maximum common side length
        common = h_dist & v_dist
        if not common:
            return -1

        max_side = max(common)
        return (max_side * max_side) % MOD
