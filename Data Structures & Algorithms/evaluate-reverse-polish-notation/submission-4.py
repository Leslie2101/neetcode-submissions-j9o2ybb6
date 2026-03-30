class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for token in tokens:
            print(stack)
            if token.isdigit() or token[1:].isdigit():
                stack.append(int(token))
            else:
                snd = stack.pop()
                fst = stack.pop()

                opMap = {
                    "+": lambda x, y: x + y,
                    "-": lambda x, y: x-y,
                    "*": lambda x, y: x*y,
                    "/": lambda x, y: (abs(x)//abs(y)) * (x//abs(x)) * (y//abs(y)) if x!= 0 and y!=0 else 0
                }

                stack.append(opMap[token](fst, snd))
        
        return stack.pop()
