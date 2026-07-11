class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n==1:
            return 1
        return (self.findTheWinner(n-1,k)+k-1)%n+1