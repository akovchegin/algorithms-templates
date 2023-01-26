from typing import Tuple

def get_sum(first_number: str, second_number: str) -> str:
    leading_zeros = '0'*abs(len(first_number)-len(second_number))
    if len(first_number) > len(second_number):
        second_number = leading_zeros + second_number
    else:
        first_number = leading_zeros + first_number
    result = ''
    for i in range(-1,0,-1):
        if int(first_number[i])+int(second_number[i]) > 1:
            result = '0' + result
            transfer = 1
        else:
            result = str(int(first_number[i])+int(second_number[i])) + result
    return result

def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number

first_number, second_number = read_input()
print(get_sum(first_number, second_number))
