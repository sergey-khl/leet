import math

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        out = 0
        while x > 1:
            out = out*10+x%10
            x /= 10

        return int(out)

sol = Solution();
print(sol.reverse(160))