import sys
from utils import read_and_load_input

def evaluate_without_precedence(expression):
    number, nested = 0, []
    for ch in '(' + expression + ')':
        if ch.isdigit():
            number = 10 * number + int(ch)
        elif ch == '(':
            nested.append([0, '+'])
        elif ch in '+*)':
            result, operator = nested[-1]
            if operator == '+':
                result += number
            elif operator == '*':
                result *= number
            nested[-1] = [result, ch]
            number = nested.pop()[0] if ch == ')' else 0
    return number

def evaluate_with_precedence(expression):
    number, nested = 0, []
    for ch in '(' + expression + ')':
        if ch.isdigit():
            number = 10 * number + int(ch)
        elif ch == '(':
            nested.append([1, 0, '+'])
        elif ch in '+*)':
            result, previous, operator = nested[-1]
            if operator == '+':
                previous += number
            elif operator == '*':
                result *= previous
                previous = number
            nested[-1] = [result, previous, ch]
            number = result * nested.pop()[1] if ch == ')' else 0
    return number

def operation_order_1():
    input = read_and_load_input("DAY18")
    return sum(evaluate_without_precedence(expression) for expression in input)

def operation_order_2():
    input = read_and_load_input("DAY18")
    return sum(evaluate_with_precedence(expression) for expression in input)


if __name__ == '__main__':
    print(f"Solution 1: {operation_order_1()}")
    print(f"Solution 2: {operation_order_2()}")
