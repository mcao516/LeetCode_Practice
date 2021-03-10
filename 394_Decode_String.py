class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                # extract the word
                e = stack.pop(-1)
                extracted = []
                
                while e != '[':
                    extracted.append(e)
                    e = stack.pop(-1)
                
                # extract k
                k = ''
                while len(stack) > 0 and stack[-1].isdigit():
                    k += stack.pop(-1)
                
                # add back to the stack
                for i in range(int(k[::-1])):
                    stack = stack + extracted[::-1]
                    
        return ''.join(stack)