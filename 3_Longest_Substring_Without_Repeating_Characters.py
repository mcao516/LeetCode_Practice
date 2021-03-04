class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        F[i] = F[i - 1]
        """
        if s == "":
            return 0
        
        F = [0] * len(s)
        
        F[0] = 1
        for i in range(1, len(s)):
            if s[i] in s[i - F[i-1]:i]:
                pre_str = s[i - F[i-1]:i]
                index = pre_str.find(s[i])
                F[i] = F[i-1] - index 
            else:
                F[i] = F[i-1] + 1
                
        return max(F)