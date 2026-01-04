class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def sum_if_four(n):
            divisors = set()
            i = 1
            
            while i * i <= n:
                if n % i == 0:
                    divisors.add(i)
                    divisors.add(n // i)
                    if len(divisors) > 4:
                        return 0
                i += 1
            
            return sum(divisors) if len(divisors) == 4 else 0

        total = 0
        for num in nums:
            total += sum_if_four(num)

        return total
