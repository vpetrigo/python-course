#!/usr/bin/env python3
# coding=utf-8

class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.sequence = list()
        self.counter = 0

    def add(self, *a):
        # добавить следующую часть последовательности
        self.counter += len(a)
        self.sequence.extend(a)

        while self.counter - 5 >= 0:
            print(sum(self.sequence[:5]))
            self.sequence = self.sequence[5:]
            self.counter -= 5

    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности
        # в порядке, в котором они были добавлены
        return self.sequence

def test():
    buf = Buffer()
    buf.add(1, 2, 3)
    assert buf.get_current_part() == [1, 2, 3] # вернуть [1, 2, 3]
    buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
    assert buf.get_current_part() == [6] # вернуть [6]
    buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
    assert buf.get_current_part() == [] # вернуть []
    buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
    assert buf.get_current_part() == [1] # вернуть [1]


if __name__ == "__main__":
    test()
