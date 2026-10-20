class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        ans = 0
        num = 0
        sign = 1

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)

            elif c == '+':
                ans += sign * num
                num = 0
                sign = 1

            elif c == '-':
                ans += sign * num
                num = 0
                sign = -1

            elif c == '(':
                stack.append(ans)
                stack.append(sign)
                ans = 0
                sign = 1

            elif c == ')':
                ans += sign * num
                num = 0

                ans *= stack.pop()
                ans += stack.pop()

        return ans + sign * num
                    
                    

           
            


                


     
        