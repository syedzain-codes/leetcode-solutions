class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        path=[]
        ans=[]
        
        def backtrack(start):
            if len(path)==k:
                ans.append(path[:])
                return

            for i in range(start,n+1):
                path.append(i)
                backtrack(i+1)
                path.pop()
        backtrack(1)
        return ans
            

        