expressions = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
    '%': lambda a, b: a / b
}


def poland_calc(expr, a, b):
    assert expr in expressions
    a, b = int(a), int(b)
    return expressions[expr](a, b)
    
values = input('Введите выражение в польской нотации: ')
expr, v1, v2 = values.split()
result = poland_calc(expr, v1, v2)
print('Ответ:', result)