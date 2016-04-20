#!/usr/bin/env python3
# coding=utf-8

class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError("only positive numbers available")
        super().append(x)

def test():
    pl = PositiveList([1, 2, 3, 4])
    assert len(pl) == 4

    try:
        pl.append(0)
    except NonPositiveError:
        print("Correct work")

    try:
        pl.append(-1)
    except NonPositiveError:
        print("Correct work")

if __name__ == "__main__":
    test()
