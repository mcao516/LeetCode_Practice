class Solution:
    def longestPalindrome(self, s: str) -> str:
        # F(i, j) = F(i-1, j-1) and s[i] == s[j]
        n = len(s)
        F = [[False] * n for _ in range(n)]
        
        max_length = 1
        max_i = 0

        for l in range(n):
            for i in range(n):
                j = i + l
                
                if j >= len(s):
                    break
                    
                if i == j:
                    F[i][j] = True
                elif j - i == 1:
                    F[i][j] = (s[i] == s[j])
                else:
                    F[i][j] = (F[i+1][j-1] and s[i] == s[j])
                    
                if F[i][j] and l + 1 > max_length:
                    max_length = l + 1
                    max_i = i
        
        return s[max_i: max_length + max_i]


class Solution2:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]
