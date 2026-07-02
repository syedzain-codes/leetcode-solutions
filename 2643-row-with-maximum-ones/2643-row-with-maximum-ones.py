class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        maxcount=0
        maxrow=0

        for i in range(0,len(mat)):
            count=0
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    count+=1
            if count>maxcount:
                maxcount=count
                maxrow=i
        ans=[maxrow,maxcount]
        return ans


        