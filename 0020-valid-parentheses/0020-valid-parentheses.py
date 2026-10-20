class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        x={')':'(',']':'[','}':'{'}
        stack=[]
        if len(s)==1:
            return False
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                
                if stack.pop()==x[i]:
                    continue
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
                 

        