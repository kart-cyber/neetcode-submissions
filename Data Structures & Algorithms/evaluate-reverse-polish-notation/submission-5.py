class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:

            if n in "+-*/":
                b = int(stack.pop())
                a = int(stack.pop())
                if n == "+":
                    c = a + b
                    stack.append(c)
                if n == "-":
                    c = a - b
                    stack.append(c)
                if n == "*":
                    c = a * b
                    stack.append(c)
                if n == "/":
                    c = int(a/b)
                    stack.append(c)
            else:
                stack.append(n)
        return int(stack[-1])
