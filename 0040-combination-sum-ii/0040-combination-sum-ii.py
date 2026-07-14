class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        seen=set()
    
        path=[]
        ans=[]
        candidates.sort()
        def backtrack(start,curr_sum):
            if curr_sum>target or start>len(candidates) or tuple(path[:]) in seen:
                return
            if curr_sum == target:
                if tuple(path) not in seen:
                    ans.append(path[:])
                    seen.add(tuple(path))
                return
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                                    continue
                path.append(candidates[i])
                backtrack(i+1,candidates[i]+curr_sum)
                path.pop()
        backtrack(0,0)
        return ans
        