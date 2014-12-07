#
# https://oj.leetcode.com/problems/single-number-ii/
#
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        A.sort()
        length = len(A)
        for idx in range(0, length - 2, 3):
            if A[idx] != A[idx +2]:
                return A[idx]
        return A[length - 1]

if __name__ == "__main__":
    ins = Solution()
    A = [1,2,2,2,1,1,3,4,3,4,3]
    print ins.singleNumber(A)