# Номер успешной отправки 81885132
import sys
from operator import add, floordiv, mul, sub


OPERATION = {
        '+': add,
        '/': floordiv,
        '*': mul,
        '-': sub
    }


class StackManagementError(Exception):
    pass


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class CalcStack:
    def __init__(self):
        self.__head = None

    def push_back(self, node):
        if self.__head is None:
            self.__head = node
            return
        current_node = self.__head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node

    def pop_back(self):
        if self.__head is None:
            raise StackManagementError(
                'Can\'t get value from empty stack. '
                'Check if you entered operands correctly.'
            )
        if self.__head.next is None:
            pop_item = self.__head.data
            self.__head = None
        else:
            previous_node = self.__head
            current_node = previous_node.next
            while current_node.next is not None:
                previous_node = current_node
                current_node = current_node.next
            pop_item = current_node.data
            previous_node.next = None
        return pop_item


def read_input():
    return sys.stdin.readline().strip().split()

def main():
    in_expression = read_input()
    calc = CalcStack()
    for item in in_expression:
        if item in OPERATION:
            y = calc.pop_back()
            x = calc.pop_back()
            result = OPERATION[item](x,y)
            calc.push_back(Node(result))
        else:
            try:
                opearnd = int(item)
            except ValueError:
                print('Operand should be a number')
                raise
            calc.push_back(Node(opearnd))
    return calc.pop_back()

if __name__ == '__main__':
    result = main()
    print(result)