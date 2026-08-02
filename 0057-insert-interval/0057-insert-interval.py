class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort()
        ans=[]
        for i in range(0,len(intervals)):
            if len(ans)==0:
                ans.append(intervals[i])
                continue
            if intervals[i][0]<=ans[len(ans)-1][1]:
                ans[len(ans)-1]=[min(ans[len(ans)-1][0],intervals[i][0]),max(ans[len(ans)-1][1],intervals[i][1])]
            else:
                ans.append(intervals[i])
        return ans
        