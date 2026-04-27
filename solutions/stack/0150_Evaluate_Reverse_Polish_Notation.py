class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        operators = {'+', '-', '*', '/'} #set is faster
        for op in tokens:   
            if op in operators:
                op1 = operands.pop()
                op2 = operands.pop()
                if op == '+':
                    operands.append(op2 + op1)
                elif op  == '-':
                    operands.append(op2 - op1)
                elif op == '*':
                    operands.append(op2 * op1)
                elif op == '/':
                    operands.append(int(op2 / op1))
            else:
                operands.append(int(op))
        return operands[0]
