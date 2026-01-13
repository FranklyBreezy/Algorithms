class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        # Total area of all squares
        total_area = 0.0
        for _, _, l in squares:
            total_area += l * l

        target = total_area / 2.0

        # Binary search bounds
        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)

        def area_below(y):
            """Compute total area below horizontal line y"""
            area = 0.0
            for _, yi, li in squares:
                # Height of square below the line
                h = min(max(y - yi, 0.0), li)
                area += li * h
            return area

        # Binary search for minimum y where area_below(y) >= target
        for _ in range(60):  # enough for 1e-5 precision
            mid = (low + high) / 2.0
            if area_below(mid) < target:
                low = mid
            else:
                high = mid

        return low
