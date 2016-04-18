'''
Реализуйте структуру данных, представляющую собой расширенную структуру стек.
Необходимо поддерживать добавление элемента на вершину стека, удаление с вершины
стека, и необходимо поддерживать операции сложения, вычитания, умножения и
целочисленного деления.

Операция сложения на стеке определяется следующим образом. Со стека снимается
верхний элемент (top1), затем снимается следующий верхний элемент (top2), и
затем как результат операции сложения на вершину стека кладется элемент, равный
top1 + top2.

Аналогичным образом определяются операции вычитания (top1 - top2), умножения
(top1 * top2) и целочисленного деления (top1 // top2).

Реализуйте эту структуру данных как класс ExtendedStack, отнаследовав его от
стандартного класса list.
Требуемая структура класса:

class ExtendedStack(list):
    def sum(self):
        # операция сложения

    def sub(self):
        # операция вычитания

    def mul(self):
        # операция умножения

    def div(self):
        # операция целочисленного деления
'''
#!/usr/bin/env python3
# coding=utf-8

class ExtendedStack(list):
    def sum(self):
        op1, op2 = self.pop(), self.pop()
        self.append(op1 + op2)

    def sub(self):
        op1, op2 = self.pop(), self.pop()
        self.append(op1 - op2)

    def mul(self):
        op1, op2 = self.pop(), self.pop()
        self.append(op1 * op2)

    def div(self):
        op1, op2 = self.pop(), self.pop()
        self.append(op1 // op2)

def test():
    ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
    ex_stack.div()
    assert ex_stack.pop() == 2
    ex_stack.sub()
    assert ex_stack.pop() == 6
    ex_stack.sum()
    assert ex_stack.pop() == 7
    ex_stack.mul()
    assert ex_stack.pop() == 2
    assert len(ex_stack) == 0

if __name__ == "__main__":
    test()
