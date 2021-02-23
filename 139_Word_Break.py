class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        F(j) = F(j - w) if w exits
        
        """
        n = len(s)
        F = [False] * n
        
        for i in range(n):
            for w in wordDict:
                if i + 1 < len(w):
                    F[i] = False
                elif i + 1 == len(w) and s[0: i+1] == w:
                    F[i] = True
                elif i+1-len(w) >= 0 and w == s[i+1-len(w): i+1]:
                    F[i] = True and F[i-len(w)]
                    
                if F[i]: break
                        
        return F[n-1]
