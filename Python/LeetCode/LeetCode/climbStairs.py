#
# https://oj.leetcode.com/problems/climbing-stairs/
#
class Solution:
    # @param n, an integer
    # @return an integer
    dict = {}
    def climbStairs(self, n):
        ret = self.dict.get(n)
        if None != ret:
            return ret

        if n == 0 or n == 1:
            return 1
        else:
            ret = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            self.dict[n] = ret
            return ret

if "__main__" == __name__:
    ins = Solution()
    print ins.climbStairs(35)