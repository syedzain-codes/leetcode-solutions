class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrammap=defaultdict(list)
        for i in strs:
            arr=[0]*26
            for c in i:
                arr[ord(c)-ord('a')]+=1
            anagrammap[tuple(arr)].append(i)
        return list(anagrammap.values())
                
      
                

        