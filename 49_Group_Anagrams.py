from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        table = defaultdict(list)
        for s in strs:
            F= [0] * 26
            for c in s:
                F[ord(c) - ord('a')] += 1
                
            key = tuple(F)
            table[key].append(s)
            
        return [v for v in table.values()]
    
    
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        table = defaultdict(list)
        for s in strs:
            F= [''] * 26
            for c in s:
                F[ord(c) - ord('a')] += c
                
            key = ''.join(F)
            table[key].append(s)
            
        return [v for v in table.values()]