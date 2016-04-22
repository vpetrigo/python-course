#!/usr/bin/env python3
# coding=utf-8

import math
import itertools

def isprime(x):
    if x <= 1:
        return False

    n = int(math.sqrt(x))
    for i in range(2, n + 1):
        if x % i == 0:
            return False
    else:
        return True


def primes():
    n = 2
    while True:
        if isprime(n):
            yield n
        n += 1

def test():
    assert isprime(0) == False
    assert isprime(1) == False
    assert isprime(2) == True
    assert isprime(3) == True
    assert isprime(4) == False
    assert isprime(17) == True

    res = list(itertools.takewhile(lambda x: x <= 3, primes()))
    assert res == [2, 3]
    res = list(itertools.takewhile(lambda x: x <= 31, primes()))
    assert res == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

if __name__ == "__main__":
    test()
