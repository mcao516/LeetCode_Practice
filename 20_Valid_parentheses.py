class Solution:
    pairs = {
        '(': ')',
        '{': '}', 
        '[': ']'
    }
    
    def isValid(self, s: str) -> bool:
        queue = []
        for c in s:
            if c in self.pairs.keys():
                queue.append(c)
            elif c in self.pairs.values():
                if len(queue) == 0: return False
                if self.pairs[queue.pop()] != c:
                    return False
        
        return len(queue) == 0