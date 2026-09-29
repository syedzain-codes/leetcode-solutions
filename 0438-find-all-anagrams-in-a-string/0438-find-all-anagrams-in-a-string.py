class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        pcount=[0]*26
        scount=[0]*26
        ans=[]
        for i in p:
            pcount[ord(i)-ord('a')]+=1
        l=0
        r=l
        while(r<len(s)):
            scount[ord(s[r])-ord('a')]+=1
            
            if r-l+1==len(p):
                if scount==pcount:
                    ans.append(l)
                scount[ord(s[l])-ord('a')]-=1
                l+=1
            r+=1
        return ans
            
            
            


    
    
        