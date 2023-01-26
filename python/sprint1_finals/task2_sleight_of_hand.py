# ID успешной посылки 81387997
import sys

def read_input():
    k = int(input())
    arr = [sys.stdin.readline().strip() for _ in range(4)]
    flat_arr = [item for sublist in arr for item in sublist]
    return k, flat_arr

def main():
    k, arr = read_input()
    keys_count=[0]*9
    for item in arr:
        if item != '.':
            keys_count[int(item)-1] += 1
    result = 0
    for key in keys_count:
        if 0 < key <= 2*k:
            result += 1
    return result

if __name__ == '__main__':
    result = main()
    print(result)
