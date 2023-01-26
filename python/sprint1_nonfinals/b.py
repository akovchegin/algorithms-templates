def check_parity(a: int, b: int, c: int) -> bool:
    result_set = set()
    for num in [a, b, c]:
        result_set.add(num%2)
        if len(result_set) > 1:
            return False
    return True

def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")

a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
