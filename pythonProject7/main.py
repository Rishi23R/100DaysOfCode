
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    n1 = float(input('what is the first number?:'))
    for operator in operations:
        print(operator)
    end=False
    while not end:
        operator = input('Pick an operation:')
        n2 = float(input('whats the next number?:'))
        calc_func = operations[operator]
        final_result = round(calc_func(n1, n2),2)
        print(f'the result of{n1} {operator} {n2} is{final_result}')
        should_continue = input(f'press\'y\' to continue with {final_result} or press\'n\' to start with 0:')
        if should_continue == 'n':
            end = True
            calculator()
        else:
            n1 = final_result

calculator()
