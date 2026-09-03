class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brack_dict = {"}":"{",  ")":"(", "]":"[" }
        #creating a for loop to push all the open brackets into the stack
        for char in s:
            if char in "({[":
                stack.append(char)
            elif char in "})]":
                if not stack or stack[-1] != brack_dict[char]:
                    return False
                stack.pop()
        if bool(stack) == True:
            return False      
        return True