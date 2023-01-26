def is_power_of_four(number: int) -> bool:
    if number == 1:
        return True
    while number%4 == 0:
        number = number / 4
        if number == 1:
            return True
    return False

print(is_power_of_four(int(input())))
