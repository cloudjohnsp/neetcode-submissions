class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            match i:
                case '+':
                    sum_res = (stack.pop() + stack.pop())
                    stack.append(sum_res)
                case '-':
                    first = stack.pop()
                    last = stack.pop()
                    sub_res = (last - first)
                    stack.append(sub_res)
                case '*':
                    times_res = (stack.pop() * stack.pop())
                    stack.append(times_res)
                case '/':
                    divisor = stack.pop()
                    dividend = stack.pop()
                    div_res = int(dividend/divisor)
                    stack.append(div_res)
                case _:
                    stack.append(int(i))
        return stack.pop()