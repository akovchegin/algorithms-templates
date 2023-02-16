import sys


def read_input():
    n = input()
    arr = sys.stdin.readline().strip().split()
    return n, arr

def bubble_sort(n, arr):
    pass

if __name__ == '__main__':
    n, arr = read_input()
    print(bubble_sort(n, arr))