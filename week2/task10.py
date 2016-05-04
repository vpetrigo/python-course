#!/usr/bin/env python3
# coding=utf-8

def mod_checker(x, mod=0):
    return lambda y: y % x == mod

def test():
    mod_3 = mod_checker(3)
    assert mod_3(3) == True
    assert mod_3(4) == False

    mod_3_1 = mod_checker(3, 1)
    assert mod_3_1(3) == False
    assert mod_3_1(4) == True

if __name__ == "__main__":
    test()
