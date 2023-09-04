class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        pos = True
        
        if len(s) > 0:
            if s[0] == '-':
                pos = False
                
            if s[0] == '+' or s[0] == '-':
                s = s[1:]
            if s == '0':
                return 0
            end = len(s)
            for i in range(len(s)):
                try:
                    int(s[i])
                except:
                    end = i 
                    break
            if end == 0:
                return 0

            out = int(s[:end]) if pos else -int(s[:end])
            if out > 2**31-1:
                return 2**31-1
            elif out < -2**31:
                return -2**31
            else:
                return out
        else:
            return 0
            

sol = Solution()
print(sol.myAtoi('words -02 with words'))
