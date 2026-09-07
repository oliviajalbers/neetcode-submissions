class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for paren in s:
            print(stack)
            if (paren == "(") or (paren == "{") or (paren == "["):
                stack.append(paren)
            elif (paren == ")"):
                if (len(stack) > 0 and stack[-1] == "("):
                    stack.pop()
                else:
                    return False
            elif (paren == "}"):
                if (len(stack) > 0 and stack[-1] == "{"):
                    stack.pop()
                else:
                    return False
            else:
                if (len(stack) > 0 and stack[-1] == "["):
                    stack.pop()
                else:
                    return False
        if (len(stack) > 0):
            return False
        
        return True

        