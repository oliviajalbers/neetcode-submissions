class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")" : "(", "}" : "{", "]" : "["}
        for paren in s:
            if paren in pairs:
                if stack and stack[-1] == pairs[paren]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(paren)
            
        return True if not stack else False
        

        