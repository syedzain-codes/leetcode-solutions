class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if ransomNote==magazine:
            return True
        if len(ransomNote)>len(magazine):
            return False
        count = [0] * 26

        for c in magazine:
            count[ord(c) - ord('a')] += 1

        for c in ransomNote:
            index = ord(c) - ord('a')

            if count[index] == 0:
                return False

            count[index] -= 1

        return True