#!/usr/bin/env python3
# coding=utf-8

class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        return True if self.coins + v <= self.capacity else False

    def add(self, v):
        # положить v монет в копилку
        self.coins += v

def test():
    a = MoneyBox(0)
    assert a.coins == 0
    assert a.can_add(1) == False

    b = MoneyBox(10)
    assert b.coins == 0
    assert b.can_add(10) == True
    b.add(10)
    assert b.coins == 10
    assert b.can_add(10) == False



if __name__ == "__main__":
    test()
