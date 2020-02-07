import unittest


def max_price_possible(N, possible_days, times, prices):
    if len(possible_days) == 0:
        return 0

    day = possible_days[0]

    max_price_without_day = max_price_possible(
        N, possible_days[1:], times, prices)

    if day + times[day] > N:
        return max_price_without_day

    excluded_days = [day + i for i in range(times[day])]
    new_possible_days = [i for i in possible_days if i not in excluded_days]

    max_price_with_day = prices[day] + \
        max_price_possible(N, new_possible_days, times, prices)

    return max(max_price_with_day, max_price_without_day)


def max_price(N, times, prices):
    return max_price_possible(N, list(range(N)), times, prices)


if __name__ == "__main__":
    N = int(input())
    T = [0] * N
    P = [0] * N
    for i in range(N):
        T[i], P[i] = map(int, input().split(' '))

    print(max_price(N, T, P))
