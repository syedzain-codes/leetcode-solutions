class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in range(0,len(matrix)):

            l=0
            r=len(matrix[0])-1
            
            while(l<=r):
                mid=l+(r-l)//2  
                if(matrix[i][mid]>target):
                    r=mid-1
                if(matrix[i][mid]<target):
                    l=mid+1
                if(matrix[i][mid]==target):
                    return True
        return False 
        