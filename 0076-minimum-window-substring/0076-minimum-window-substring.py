class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s==t:
            return s
        tc=[0]*256
        sc=[0]*256
        minlen=len(s)+1
        ans=""
        req=0

        for i in t:
            tc[ord(i)]+=1
        for i in range(256):
           if tc[i]>0:

            req+=1


            
        left=0
        right=0
        formed=0
        while(right<len(s)):
            idx = ord(s[right])
            sc[ord(s[right])]+=1
            if tc[idx] > 0 and sc[idx] == tc[idx]:
                formed += 1
            
            while formed==req:
                    
                if right - left + 1 < minlen:
                    minlen = right - left + 1
                    ans = s[left:right + 1]

                idx = ord(s[left])
                sc[idx] -= 1

                if tc[idx] > 0 and sc[idx] < tc[idx]:
                    formed -= 1

                left += 1
    
                
                

            right+=1
        return str(ans)

            
      


            
            
        
        