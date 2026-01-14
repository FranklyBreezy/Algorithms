class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """

        # Build sweep events and collect x-coordinates
        events = []
        xs = set()

        for x, y, l in squares:
            events.append((y, 1, x, x + l))      # add interval
            events.append((y + l, -1, x, x + l)) # remove interval
            xs.add(x)
            xs.add(x + l)

        xs = sorted(xs)
        x_index = {x: i for i, x in enumerate(xs)}
        events.sort()

        # Segment Tree for union length of x-intervals
        n = len(xs) - 1
        count = [0] * (4 * n)
        length = [0] * (4 * n)

        def push_up(node, l, r):
            if count[node] > 0:
                length[node] = xs[r] - xs[l]
            elif l + 1 == r:
                length[node] = 0
            else:
                length[node] = length[node * 2] + length[node * 2 + 1]

        def update(ql, qr, val, node=1, l=0, r=n):
            if qr <= l or r <= ql:
                return
            if ql <= l and r <= qr:
                count[node] += val
                push_up(node, l, r)
                return
            mid = (l + r) // 2
            update(ql, qr, val, node * 2, l, mid)
            update(ql, qr, val, node * 2 + 1, mid, r)
            push_up(node, l, r)

        # Sweep function
        def sweep(target=None):
            area = 0
            prev_y = events[0][0]
            i = 0

            while i < len(events):
                y = events[i][0]
                dy = y - prev_y
                width = length[1]

                if dy > 0:
                    strip_area = width * dy
                    if target is not None and area + strip_area >= target:
                        return prev_y + (target - area) / width
                    area += strip_area

                while i < len(events) and events[i][0] == y:
                    _, typ, xl, xr = events[i]
                    update(x_index[xl], x_index[xr], typ)
                    i += 1

                prev_y = y

            return area

        total_area = sweep()
        return sweep(total_area / 2.0)
