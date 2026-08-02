class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def square(x):
            ans=0
            
            while(x>0):
                rem=x%10
                ans+=(rem**2)
                x=x//10
            return ans
        slow=square(n)
      
        fast=square(square(n))
        if slow==1 or fast==1:
            return True
        while(slow!=fast):
            slow=square(slow)
            fast=square(square(fast))
            if slow==1 or fast==1:
                return True
        return False


        