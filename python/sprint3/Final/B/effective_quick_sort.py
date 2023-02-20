import sys


class Participant():
    def __init__(self, username, tasks, penalty):
        self.params = (int(tasks), int(penalty), username)
    

    def is_winner(self, in_value):
        value1 = (self.params[0] * -1, self.params[1], self.params[2])
        value2 = (in_value.params[0] * -1, in_value.params[1], in_value.params[2])
        return value1 <= value2

    def __str__(self):
        return f'{self.params[0]},{self.params[1]},{self.params[2]}'
    

def read_input():
    n = int(input())
    arr = [
        Participant(*sys.stdin.readline().strip().split()) for _ in range(n) 
    ]
    return n, arr


def quick_sort(arr, left, right):
    if right <= left:
        return arr
    mid = (right + left) // 2
    pivot = arr[mid]
    i = left
    j = right
    while i < j:
        if not arr[i].is_winner(pivot) and arr[j].is_winner(pivot):
            arr[i], arr[j] = arr[j], arr[i]
        if arr[i].is_winner(pivot):
            i += 1
        if not arr[j].is_winner(pivot):
            j -= 1
    quick_sort(arr, left, i-1)
    quick_sort(arr, i+1, right)


if __name__ == '__main__':
    n, arr = read_input()
#    print(*arr)
    quick_sort(arr, 0, n-1)
    print(*arr)