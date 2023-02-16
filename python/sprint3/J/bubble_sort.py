import sys


def read_input():
    n = int(input())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    return n, arr

def bubble_sort(n, arr):
    for j in range(n-1,0,-1):
        permutations = 0
        for i in range(j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                permutations += 1
        if permutations:
            print(*arr)
        else:
            if j == n-1:
                print(*arr)
            return


if __name__ == '__main__':
    n, arr = read_input()
    bubble_sort(n, arr)
