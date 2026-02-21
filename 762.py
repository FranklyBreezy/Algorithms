class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # Possible prime counts up to 20 (since right <= 10^6)
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        
        count = 0
        for num in range(left, right + 1):
            # Count set bits using built-in function
            if bin(num).count('1') in primes:
                count += 1
                
        return count