#
# https://oj.leetcode.com/problems/search-insert-position/
#
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        length = len(A)
        if target < A[0]:
            return 0
        
        if target > A[length - 1]:
            return length

        max = len(A) - 1
        min = 0
        mid = 0
        while min <= max:
            mid = min + (max - min) / 2
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                max = mid - 1
            elif A[mid] < target:
                min = mid + 1
        if min > max:
            return min
        else:
            return max

if __name__ == "__main__":
    ins = Solution()
    A= [1,3,5,6]

    #print ins.searchInsert(A, 5)
    print ins.searchInsert(A, 2)
    #print ins.searchInsert(A, 7)
    #print ins.searchInsert(A, 0)