class Solution:
    def longestBalanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Segment Tree Arrays (4 * N size)
        # We store min_val and max_val to quickly check if 0 exists in a range
        self.mn = [0] * (4 * n)
        self.mx = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        
        last_pos = {}
        ans = 0

        for i, x in enumerate(nums):
            # Determine contribution: +1 if Even, -1 if Odd
            val = 1 if x % 2 == 0 else -1
            
            # Find the previous occurrence of this number
            prev = last_pos.get(x, -1)
            
            # Update the range [prev + 1, i] with the new contribution
            # This affects all subarrays ending at i that start after 'prev'
            self.update(1, 0, n - 1, prev + 1, i, val)
            
            # Update last position
            last_pos[x] = i
            
            # Find the smallest L in [0, i] where Score[L] == 0
            l_idx = self.query_first_zero(1, 0, n - 1, 0, i)
            
            if l_idx != -1:
                ans = max(ans, i - l_idx + 1)
                
        return ans

    def push(self, node):
        if self.lazy[node] != 0:
            lz = self.lazy[node]
            left, right = 2 * node, 2 * node + 1
            
            # Apply lazy to children
            self.lazy[left] += lz
            self.mn[left] += lz
            self.mx[left] += lz
            
            self.lazy[right] += lz
            self.mn[right] += lz
            self.mx[right] += lz
            
            # Reset lazy for current node
            self.lazy[node] = 0

    def update(self, node, start, end, l, r, val):
        if l > end or r < start:
            return
        
        if l <= start and end <= r:
            self.mn[node] += val
            self.mx[node] += val
            self.lazy[node] += val
            return
        
        self.push(node)
        mid = (start + end) // 2
        self.update(2 * node, start, mid, l, r, val)
        self.update(2 * node + 1, mid + 1, end, l, r, val)
        
        self.mn[node] = min(self.mn[2 * node], self.mn[2 * node + 1])
        self.mx[node] = max(self.mx[2 * node], self.mx[2 * node + 1])

    def query_first_zero(self, node, start, end, l, r):
        if l > end or r < start:
            return -1
        
        # Optimization: If 0 is not within the value range of this node, skip it.
        # This relies on the property that values change by at most 1 between adjacent indices,
        # ensuring we don't skip a 0 if min <= 0 <= max.
        if self.mn[node] > 0 or self.mx[node] < 0:
            return -1
        
        if start == end:
            return start if self.mn[node] == 0 else -1
            
        self.push(node)
        mid = (start + end) // 2
        
        # Try left child first to find the smallest index (longest subarray)
        res = self.query_first_zero(2 * node, start, mid, l, r)
        if res != -1:
            return res
            
        return self.query_first_zero(2 * node + 1, mid + 1, end, l, r)