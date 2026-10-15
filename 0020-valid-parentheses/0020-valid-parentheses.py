class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        x={'(':')','[':']','{':'}'}
        stack=[]
        for i in range(0,len(s)):
            if s[i] in x:
                stack.append(s[i])

            if s[i] not in x and len(stack)==0:
                return False
            if s[i] not in x and x[stack.pop()]!=s[i]:
                return False
        if len(stack)==0:
            return True
        else:
            return False
        