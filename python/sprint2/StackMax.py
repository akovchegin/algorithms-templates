import sys


class Stack:
    def __init__(self):
        self.stack = []
        self.max_value = None

    def push(self, value):
<<<<<<< HEAD
        self.stack.append(value)
    
    def pop(self):
        if len(self.stack) == 0:
            print('error')
=======
        self.stack.append(int(value))
    
    def pop(self):
        if len(self.stack) == 0:
            return 'error'
>>>>>>> 390ccc9401d4a9fb2dd08f6c520d832df78c193a
        else:
            self.stack.pop()
    
    def get_max(self):
        if len(self.stack) == 0:
<<<<<<< HEAD
            return None
        max_value = int(self.stack[0])
        for value in self.stack[1:]:
            if int(value) > max_value:
                max_value = int(value)
        return max_value
=======
            return 'None'
        self.max_value = self.stack[0]
        for value in self.stack[1:]:
            if int(value) > self.max_value:
                self.max_value = int(value)
        return self.max_value
>>>>>>> 390ccc9401d4a9fb2dd08f6c520d832df78c193a


def read_input():
    num_commands = int(input())
    command_list = [sys.stdin.readline().strip() for _ in range(num_commands)]
    return command_list

def main():
    command_list = read_input()
    stack = Stack()
<<<<<<< HEAD
    for command in command_list:
        if command.startswith('push'):
            stack.push(command.split()[1])
        if command == 'pop':
            stack.pop()
        if command == 'get_max':
            print(stack.get_max())
=======
    execute_command = {
        'push': stack.push,
        'pop': stack.pop,
        'get_max': stack.get_max
    }
    for idx, cmd in enumerate(command_list):
        result = None
        cmd_name = cmd.split()[0]
        cmd_params = cmd.split()[1:]
        result = execute_command[cmd_name](*cmd_params)
        if result is not None:
            print(result)
>>>>>>> 390ccc9401d4a9fb2dd08f6c520d832df78c193a

if __name__ == '__main__':
    main()
