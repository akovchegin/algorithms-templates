import sys


def read_input():
    num_days = int(input())
    days_arr = list(map(int, sys.stdin.readline().strip().split()))
    price = int(input())
    return num_days, days_arr, price


def find_day(arr, price, left, right):
    if arr[right] < price:
        return -1
    if left == right:
        return right
    mid = (left+right) // 2
    if arr[mid] >= price:
        return find_day(arr, price, left, mid)
    else:
        return find_day(arr, price, mid+1, right)


if __name__ == '__main__':
    num_days, days_arr, price = read_input()
    day1_idx = find_day(days_arr, price, 0, num_days-1)
    if day1_idx >= 0:
        day1 = day1_idx+1
        day2_idx = find_day(days_arr, price*2, day1_idx, num_days-1)
    else:
        day1 = day1_idx
        day2_idx = -1
    day2 = -1 if day2_idx == -1 else day2_idx+1
    print(day1, day2)