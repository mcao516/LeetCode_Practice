class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        F[i] = F[i - j] for every j in wordDict
        
        F[i]: if the first i chars is cuttable
        """
        n = len(s)
        F = [False] * (n + 1)
        
        F[0] = True
        for i in range(1, n + 1):
            cuttable = []
            for w in wordDict:
                if i >= len(w) and s[i-len(w):i] == w:
                    cuttable.append(F[i-len(w)])
            F[i] = any(cuttable)

        return F[n]
