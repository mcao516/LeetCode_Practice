class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = len(p)
        if len(s) < l: return []
        
        p_counts = tuple(self.to_tuple(p))
        
        indexs = []
        for i in range(len(s)):
            if i + l > len(s):
                break
                
            if i == 0:
                t_counts = self.to_tuple(s[:l])
            else:
                t_counts[ord(s[i-1]) - ord('a')] -= 1
                t_counts[ord(s[i+l-1]) - ord('a')] += 1

            if p_counts == tuple(t_counts):
                indexs.append(i)
                
        return indexs
            
            
    def to_tuple(self, s):
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord('a')] += 1
        return counts
            