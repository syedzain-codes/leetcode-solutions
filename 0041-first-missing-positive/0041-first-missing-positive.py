class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        w=0
        while w<n:
            j=nums[w]-1
            if 1<=nums[w]<n and nums[w]!=nums[j]:
                nums[w],nums[j]=nums[j],nums[w]
            else:
                w+=1
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1
        
        