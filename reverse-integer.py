class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)[::-1]
        out = ''
        first = True
        for i in range(len(x)):
            if x[i] == '-':
                out = '-' + out
                continue
            if x[i] != '0':
                first = False
            elif x[i] == '0' and first and len(x) > 1:
                continue
            out += x[i]
        out = int(out)
        if out > 2**31-1 or out < -2**31:
            return 0
        else:
            return out

sol = Solution();
print(sol.reverse(-120))