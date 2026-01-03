class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9+7
        a = 6
        b = 6
        for _ in range(2,n+1):
            n_a = (2*a+2*b)% MOD
            n_b = (2*a+3*b)% MOD
            a,b = n_a,n_b
        return (a+b)%MOD