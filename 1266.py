class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        time_taken = 0
        for i in range(1,len(points)):
            x1,y1 = points[i-1]
            x2,y2 = points[i]
            time_taken += max(abs(x2-x1),abs(y2-y1))
        return time_taken