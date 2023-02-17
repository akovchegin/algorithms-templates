import sys


def read_input():
    n = int(input())
    arr = sys.stdin.readline().strip().split()
    return n, arr


def is_greater(value1, value2):
    return (value1+value2) > (value2+value1)    

def selection_sort(n, arr, key):
    for i in range(0, n-1):
        for j in range(i+1, n):
            if is_greater(arr[j], arr[i]):
                arr[j], arr[i] = arr[i], arr[j]


if __name__ == '__main__':
    n, arr = read_input()
    selection_sort(n, arr, is_greater)
    print(''.join(arr))