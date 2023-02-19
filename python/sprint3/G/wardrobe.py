import sys


def read_input():
    n = int(input())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    return n, arr


def sort_clothes(n, arr):
    items_count = [0]*3
    for item in arr:
        items_count[item] += 1
    arr[:] = []
    for i in range(len(items_count)):
        arr += [i]*items_count[i]

if __name__ == '__main__':
    n, arr = read_input()
    sort_clothes(n, arr)
    print(*arr)
