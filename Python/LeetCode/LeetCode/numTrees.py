#
# https://oj.leetcode.com/problems/unique-binary-search-trees/
#
class Solution:
    # @return an integer
    def numTrees(self, n):
        if 1 >= n:
            return 1
        nums = 0
        for idx in range(n):
            nums += self.numTrees(idx) * self.numTrees(n - idx - 1)
        return nums

if __name__ == "__main__":
    ins = Solution()
    print ins.numTrees(4)