"""
Given a string representing a postfix expression (5 3 + 2 -), write a function that evaluates this expression.

Example expressions:
infix                         postfix
1 + 1 = 2                     1 1 + --> = 2                     
5 + 3 - 2                     5 3 + 2 - --> = 6                     
(1 + 3) - 4 + (5 + 6) = -1    1 3 + 4 - 5 6 - + --> = -1
                              [1, 3, +, 4, -, 5, 6, -, +]
                                    [4, 4, -,
                                         [0, 5, 6 -,
                                            [5, 6, -
                                         [0, -1, +] --> = -1
Implement:
evaluate_postfix(expression: String)--> Number
"""

import operator
# operator.truediv(a, b)
operators = {'+': operator.add,
             '-': operator.sub,
             '*': operator.mul,
             '/': (lambda x, y: x / y),
             'mod': operator.mod
            }

def evaluate_postfix(num_str):
    list_num_str = list(num_str.split())

    num_stack = []

    for num in list_num_str:
        if not num_stack or num not in operators:
            num_stack.append(num)
        if num in operators:
            operand = num
            second_num = num_stack.pop()
            first_num = num_stack.pop()
            evaluated_num = operators.get(operand)(int(first_num), int(second_num))
            num_stack.append(evaluated_num)
    
    if len(num_stack) > 1 or not num_stack:
        raise ValueError("too many elements, not enough operands OR no elements")
    if len(num_stack) == 1:
        return num_stack[0]

print(evaluate_postfix("1 3 + 4 - 5 6 - +"))