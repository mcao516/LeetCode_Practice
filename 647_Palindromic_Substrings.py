class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        F(i, j) = s[i] == s[j] and F(i-1, j-1)
        
        """
        n = len(s)
        F = [[False] * n for _ in range(n)]
        
        for i in range(n):
            F[i][i] = True
            
        for i in range(n - 1):
            if s[i] == s[i+1]:
                F[i][i+1] = True
        
        for l in range(2, n):
            for i in range(n):
                j = i + l
                
                if i + 1 >= n or j >= n:
                    break
                    
                F[i][j] = (s[i] == s[j]) and F[i+1][j-1]
                
        counter = 0
        for l in F:
            counter += sum(l)

        return counter
