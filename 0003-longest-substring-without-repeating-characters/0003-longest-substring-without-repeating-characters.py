class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen=set()
        maxlen=0
        l=0
        for r in range(0,len(s)):
            while s[r] in seen:
               
                seen.remove(s[l])
                l+=1
                
        
            seen.add(s[r])
            maxlen=max(maxlen,r-l+1)
        return maxlen
            
