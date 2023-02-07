# Номер успешной отправки 81873328
import sys


class DequeManagementError(Exception):
    pass


class CircleDeque:
    def __init__(self, max_queue_size=0):
        self.__max_queue_size = max_queue_size
        self.__items = [None] * self.__max_queue_size
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def push_back(self, data):
        if self.queue_overflow():
            raise DequeManagementError(
                'Can\'t add new element. Queue overflow'
            )
        self.__items[self.__tail] = data
        self.__tail = (self.__tail+1) % self.__max_queue_size
        self.__size += 1

    def push_front(self, data):
        if self.queue_overflow():
            raise DequeManagementError(
                'Can\'t add new element. Queue overflow'
            )
        self.__head = (self.__head-1) % self.__max_queue_size
        self.__items[self.__head] = data
        self.__size += 1

    def pop_back(self):
        if self.queue_empty():
            raise DequeManagementError(
                'Can\'t get element from the queue. Queue is empty'
            )
        pop_item = self.__items[self.__tail-1]
        self.__items[self.__tail-1] = None
        self.__tail = (self.__tail-1) % self.__max_queue_size
        self.__size -= 1
        return pop_item

    def pop_front(self):
        if self.queue_empty():
            raise DequeManagementError(
                'Can\'t get element from the queue. Queue is empty'
            )
        pop_item = self.__items[self.__head]
        self.__items[self.__head] = None
        self.__head = (self.__head+1) % self.__max_queue_size
        self.__size -= 1
        return pop_item

    def queue_overflow(self):
        return self.__size == self.__max_queue_size

    def queue_empty(self):
        return self.__size == 0


def read_input():
    num_commands = int(input())
    max_queue_size = int(input())
    commands_list = list(sys.stdin.readline().strip() for _ in range(num_commands))
    return max_queue_size, commands_list


def main():
    max_queue_size, commands_list = read_input()
    queue = CircleDeque(max_queue_size)
    execute_command = {
        'push_back': queue.push_back,
        'push_front': queue.push_front,
        'pop_back': queue.pop_back,
        'pop_front': queue.pop_front 
    }
    for command in commands_list:
        command = command.split()
        if len(command) == 2:
            result = execute_command[command[0]](command[1])
        else:
            result = execute_command[command[0]]()
        if result is not None:
            print(result)


if __name__ == '__main__':
    main()