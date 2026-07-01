class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        prev=nums[0]
        ans=1
        count=1
        for i in range(1,len(nums)):
            if nums[i]==prev:
                continue

            
            
            if nums[i]-prev==1:
                    count+=1
                    
            else:
                ans=max(count,ans)
                count=1
            prev=nums[i]
        return max(count,ans)
        
        