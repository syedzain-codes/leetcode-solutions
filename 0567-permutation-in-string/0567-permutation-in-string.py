class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        a1={}
        a2={}
        for i in s1:
            a2[i]=a2.get(i,0)+1
        l=0

        for r in range(0,len(s2)):
            a1[s2[r]] = a1.get(s2[r], 0) + 1
            if r-l+1==len(s1):
                if a1==a2:
                    return True
                left = s2[l]
                a1[left] -= 1

                if a1[left] == 0:
                    del a1[left]

                l += 1

        return False
            

        