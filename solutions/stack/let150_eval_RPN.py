from typing import List

def is_integer(s: str) -> bool:
    if s[0] == '-':
        return s[1:].isdigit()
    else:
        return s.isdigit()

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if is_integer(t):
                stack.append(int(t))
                continue
            a = stack.pop()
            b = stack.pop()
            if t == "+":
                stack.append(a + b)

            if t == "-":
                stack.append(b - a)

            if t == "*":
                stack.append(a * b)

            if t == "/":
                x = b // a
                if x < 0:
                    x = 0
                stack.append(x)

        return stack.pop()

if __name__ == '__main__':
    tokens = ["4","-2","/","2","-3","-","-"]
    a = Solution().evalRPN(tokens)
    print(a)