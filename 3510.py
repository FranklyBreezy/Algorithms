import heapq

class Solution(object):
    def minimumPairRemoval(self, nums):
        n = len(nums)
        if n <= 1:
            return 0

        # Doubly linked list
        left = [-1] + list(range(n - 1))
        right = list(range(1, n)) + [n]
        alive = [True] * n

        # Count bad adjacent pairs
        bad = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                bad += 1

        # Min heap of (sum, left_index)
        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (nums[i] + nums[i + 1], i))

        ops = 0

        while bad > 0:
            s, i = heapq.heappop(heap)

            if not alive[i]:
                continue
            j = right[i]
            if j >= n or not alive[j]:
                continue
            if s != nums[i] + nums[j]:
                continue

            # Remove old bads
            if left[i] != -1 and nums[left[i]] > nums[i]:
                bad -= 1
            if nums[i] > nums[j]:
                bad -= 1
            if right[j] < n and nums[j] > nums[right[j]]:
                bad -= 1

            # Merge
            nums[i] += nums[j]
            alive[j] = False
            ops += 1

            # Relink
            r = right[j]
            right[i] = r
            if r < n:
                left[r] = i

            # Add new bads
            if left[i] != -1 and nums[left[i]] > nums[i]:
                bad += 1
            if right[i] < n and nums[i] > nums[right[i]]:
                bad += 1

            # Push new heap entries
            if left[i] != -1:
                heapq.heappush(heap, (nums[left[i]] + nums[i], left[i]))
            if right[i] < n:
                heapq.heappush(heap, (nums[i] + nums[right[i]], i))

        return ops
