class Solution(object):
    def numSubarrayBoundedMax(self, nums, left, right):
        """
        :type nums: List[int]
        :type left: int
        :type right: int
        :rtype: int
        """
        def count(limit):
            ans = 0
            curr = 0

            for num in nums:
                if num <= limit:
                    curr += 1
                else:
                    curr = 0

                ans += curr

            return ans

        return count(right) - count(left - 1)
            
                
        