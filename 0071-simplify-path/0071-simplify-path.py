class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        ans=""
        stack=[]
        curr=""
        for c in path+'/':
            if c=="/":
                if curr=="..":

                    if stack: 
                        stack.pop()
                elif curr=="." or curr=="":
                    pass
                else:
                    stack.append(curr)
            
            
                curr=""
                
            if c!="/":
                curr+=c
        for i in stack:
            ans+="/"+i
        if ans=="":
            return "/"
        return ans
           
        