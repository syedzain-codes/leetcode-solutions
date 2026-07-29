class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        
        ans = []
        prev = []
        
        for i in range(1, numRows + 1):          
            curr = [1] * i                       
            
            for j in range(1, i - 1):
                curr[j] = prev[j - 1] + prev[j]
            
            ans.append(curr)
            prev = curr                         
        
        return ans

                
        