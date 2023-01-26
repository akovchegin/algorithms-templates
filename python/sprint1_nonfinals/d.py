from typing import List

def get_weather_randomness(temperatures: List[int]) -> int:
    if len(temperatures) == 1:
        return 1
    result = 0
    if temperatures[0] > temperatures[1]:
        result += 1
    if temperatures[-1] > temperatures[-2]:
        result += 1
    for day in range(1, len(temperatures)-1):
        if temperatures[day] > temperatures[day+1]:
            if temperatures[day] > temperatures[day-1]:
                result += 1
            day += 2
    return result

def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures

temperatures = read_input()
print(get_weather_randomness(temperatures))
