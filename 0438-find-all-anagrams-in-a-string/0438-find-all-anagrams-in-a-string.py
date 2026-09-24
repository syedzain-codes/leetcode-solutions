class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        count=[0]*26
        for c in p:
            count[ord(c)-ord('a')]+=1
        window=[0]*26
        ans=[]
        for i in range(0,len(s)):
            window[ord(s[i])-ord('a')]+=1
            if(i>=len(p)-1):
                if count==window:
                    ans.append(i-len(p)+1)
                
                window[ord(s[i-len(p)+1])-ord('a')]-=1
        return ans
        