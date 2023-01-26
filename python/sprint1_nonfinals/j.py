from typing import List

def factorize(number: int) -> List[int]:

    is_prime = list(range(number+1))
    for num in range (2, number):
        if is_prime[num]:
            for j in range(2*num, number+1, num):
                is_prime[j] = False

#    result.sort()
#    return result
    result = []
    for i in range(len(is_prime)):
        if is_prime[i]:
            result.append(is_prime[i])

#result = factorize(int(input()))
#print(" ".join(map(str, result)))
def main():
    result = factorize(917521579)
    print(result)

if __name__ == '__main__':
    main()
