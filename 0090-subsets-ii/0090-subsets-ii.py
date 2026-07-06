class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        seen=set()
        ans=[]
        path=[]
        nums.sort()
        def backtrack(start):
            if tuple(path[:]) not in seen:
                seen.add(tuple(path[:]))
                ans.append(path[:])
            if start==len(nums):

                return
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i+1)
                path.pop()
        backtrack(0)
        return ans
        