# ID успешной посылки 81386810
import sys

def read_input():
    length = int(input())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    return length, arr

def main():
    length, arr = read_input()
    result = [0]*length
    distance = length
    for idx, value in enumerate(arr):
        distance = 0 if value == 0 else distance + 1
        result[idx] = distance
    distance = length
# Использование enumerate для обратного прохода привело к увеличению времени
# выполнения на 30%, но к уменьшению использования памяти на 25%
# enumerate: 1.617s 111.95Mb; без enumerate: 1.145s 144.88Mb
# Выбор решения видимо должен зависеть от конкретных требований к ресурсам.
    for idx, value in enumerate(reversed(arr)):
        distance = 0 if value == 0 else distance + 1
        if distance < result[length - 1 - idx]:
            result[length - 1 - idx] = distance
    return result

if __name__ == '__main__':
    result = main()
    print(*result)
