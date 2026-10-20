class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack=[]
        ans=0
        heights.append(0)
        for i in range(0,len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                height=heights[stack.pop()]
                if stack:
                   width=i-stack[-1]-1
                else:
                    width=i
                area=height*width
                ans=max(ans,area)
            stack.append(i)
        return ans                




        