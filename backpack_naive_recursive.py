class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        return self.pack(m, A)
    
    def pack(self, m, A):
        # write your code here
        if len(A) == 0 or m <= 0:
            return 0
        elif A[0] > m:
            return self.pack(m, A[1:])
        elif len(A) == 1 and A[0] <= m:
            return A[0]
        else:
            return max(self.pack(m - A[0], A[1:]) + A[0], self.pack(m, A[1:]))


print(Solution().backPack(10, [3,4,8,5]))