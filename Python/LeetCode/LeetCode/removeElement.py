class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if None == A:
            return 0
        idx = 0
        length = len(A)
        while idx < length:
            if A[idx] == elem:
                del A[idx]
                length -=1
            else:
                idx +=1

if __name__ == "__main__":
    ins = Solution()
    A = [1,2,3,4,5,6,7,7,8,8,7,7]
    ins.removeElement(A, 7)
    input()