# ID успешной отправки 82765897
import sys


class Participant():
    def __init__(self, username, tasks, penalty):
        self.__stats = (-int(tasks), int(penalty), username)

    def __lt__(self, obj):
        return self.__stats < obj.__stats
    
    def __gt__(self, obj):
        return self.__stats > obj.__stats

    def __str__(self):
        return self.__stats[2]
    

def read_input():
    n = int(input())
    arr = [
        Participant(*sys.stdin.readline().strip().split()) for _ in range(n)
    ]
    return n, arr


def __partition(arr, left, right):
    i = left
    j = right
    pivot = arr[(left+right)//2]
    while True:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        if (arr[i] == arr[j] == pivot) and i == (j-1):
            return i
        arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr, left, right):
    if left >= right:
        return
    bound = __partition(arr, left, right)
    quick_sort(arr, left, bound)
    quick_sort(arr, bound+1, right)


if __name__ == '__main__':
    n, arr = read_input()
    quick_sort(arr, 0, n-1)
    print(*arr, sep='\n')
