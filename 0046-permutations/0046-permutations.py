class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        path=[]
        seen=set()
        def backtrack():
            if len(path)==len(nums):
                ans.append(path[:])
                return
            for i in nums:
                if i in seen:
                    continue
                seen.add(i)
                path.append(i)
                backtrack()
                path.pop()
                seen.remove(i)
        backtrack()
        return ans
        
        