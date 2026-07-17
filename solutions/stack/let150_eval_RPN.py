from typing import List

def is_integer(s: str) -> bool:
    if s[0] == '-':
        return s[1:].isdigit()
    else:
        return s.isdigit()


def evalRPN(tokens: List[str]) -> int:
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
            x = int(b / a)
            stack.append(x)

    return stack.pop()

if __name__ == '__main__':
    rpn = ["4","-2","/","2","-3","-","-"]
    ans = evalRPN(rpn)
    print(ans)