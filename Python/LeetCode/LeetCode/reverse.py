#
# https://oj.leetcode.com/problems/reverse-integer/
#
class Solution:
    # @return an integer
    def reverse(self, x):
        s = str(x)
        if 0 == len(s):
            return 0

        if s[0] == "-":
            s = "-" + s[:0:-1]
        else:
            s = s[::-1]
        
        rev = int(s)
        if rev > 2147483647 or rev < -2147483647:
            return 0
        else:
            return rev


if "__main__" == __name__:
    ins = Solution()
    print ins.reverse(0)
        