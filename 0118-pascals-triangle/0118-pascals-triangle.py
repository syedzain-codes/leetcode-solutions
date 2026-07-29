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
            temp = []                     
            for j in range(1, i + 1):     
                if j == 1 or j == i:      
                    temp.append(1)
                else:                     
                    
                    temp.append(prev[j-2] + prev[j-1])
            ans.append(temp)
            prev = temp                  
        
        return ans

                
        