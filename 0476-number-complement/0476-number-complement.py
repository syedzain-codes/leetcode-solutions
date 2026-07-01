class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary=""
        if num==0:
            return 1
        while num>0:
            binary=str(num%2)+binary
            num=num//2
        flipped=""
        for i in binary:
            if i=="0":
                flipped=flipped+"1"
            else:
                flipped=flipped+"0"
        output=0
        power=len(flipped)-1
        for i in flipped:
            output+=int(i)*(2**power)
            power-=1
        return output



        