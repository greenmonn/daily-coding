def get_kth_big_element(numbers, K):
    numbers.sort()
    numbers.reverse()

    return numbers[K - 1]


def get_generatable_numbers(numbers, N):
    pass


if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        N, K = map(int, input().split(' '))

        numbers = list(input())

        candidates = get_generatable_numbers(numbers, N)

        answer = get_kth_big_element(candidates, K)

        print('#{} {}'.format(i + 1, answer))
