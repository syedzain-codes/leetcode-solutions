class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype
        : int
        """
        if sum(gas)<sum(cost):
            return -1
        fuel=0
        start=0
        
        for i in range(len(gas)):
            fuel+=gas[i]-cost[i]
            if fuel<0:
                start=i+1
                fuel=0
        return start
            

                   