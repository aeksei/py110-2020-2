import re
import operator

FILENAME = 'example.txt'
oper = {"+": operator.add}

example = re.compile(r"""
    (?P<first>\d+\.?\d*)(?:\ *)  # первое число
    (?P<operator>[+-/*])(?:\ *)  # арифметический оператор
    (?P<second>\d+\.?\d*)(?:\ *)=(?:\ *)  # второе число
    (?P<result>\d+\.?\d*)  # результат
    """, re.VERBOSE)  # скобочные группы

with open(FILENAME, 'r') as f:
    for line in f:
        result = example.fullmatch(line.rstrip())  # парсинг строки
        print(result)
        if result is not None:
            print(oper[result['operator']](float(result['first']), float(result['second'])) == float(result['result']))

