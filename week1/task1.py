import sys

def calc_sum(reader):
    result = 0
    for [i] in list(reader):
        result += i

    return result

reader = (tuple(map(int, line.split())) for line in sys.stdin)
[n] = next(reader)
print(calc_sum(reader))
