class Solution:
    mapping = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }
    
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        else:
            return self.helper(digits)
        
    def helper(self, digits):
        if len(digits) == 1:
            return self.mapping[digits]
        else:
            outputs = self.helper(digits[:-1])
            
            new_outputs = []
            last_char = digits[-1]
            for l in self.mapping[last_char]:
                for o in outputs:
                    new_outputs.append(o + l)
            return new_outputs
        
            