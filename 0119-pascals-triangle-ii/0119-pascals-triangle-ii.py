class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans=[]
        prev=[]
        for i in range(1,rowIndex+2):
            temp=[]
            for j in range(1,i+1):
                if j==1 or j==i:
                    temp.append(1)
                else:
                    temp.append(prev[j-2]+prev[j-1])
            ans.append(temp)
            prev=temp
        return ans[rowIndex]
        