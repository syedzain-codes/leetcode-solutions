class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left=0
        right=len(s)-1
        def getreverse(s,left,right):
            if left>right:
                return s
            s[left],s[right]=s[right],s[left]
            getreverse(s,left+1,right-1)
        s=getreverse(s,left,right)
        return s


        