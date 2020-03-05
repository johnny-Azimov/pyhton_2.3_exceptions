expressions = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
    '%': lambda a, b: a / b
}


assert '+' in expressions
assert '-' in expressions
assert '*' in expressions
assert '/' in expressions

def poland_calc(expr, a, b):
    assert expr in expressions
    a, b = int(a), int(b)
    return expressions[expr](a, b)


if __name__ == '__main__':
    while True:
        try:
            values = input('Введите выражение в польской нотации: ')
            expr, v1, v2 = values.split()
            result = poland_calc(expr, v1, v2)
            print('Ответ:', result)
        except ZeroDivisionError:
            print('Делить на ноль нельзя!')
        except ValueError:
            print('ValueError: недостаточно значений для распаковки ')
        except TypeError:
            print('TypeError: неподдерживаемые типы операндов для -: "str" и "str"')