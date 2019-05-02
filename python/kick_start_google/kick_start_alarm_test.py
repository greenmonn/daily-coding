import pytest


def test_get_power():
    assert 1 == get_total_power(1, [1])
    assert 20 == get_total_power(2, [1, 2])
    assert 52 == get_total_power(3, [3, 2])


def get_total_power(K, parameter_array):
    powers = 0
    for i in range(1, K+1):
        power = calculate_power_of_subarrays(i, parameter_array)
        powers += power

    return powers


def test_calculate_power_of_subarrays():
    assert 8 == calculate_power_of_subarrays(1, [1, 2])
    assert 71 == calculate_power_of_subarrays(2, [1, 4, 2])


def calculate_power_of_subarrays(i, parameter_array):
    sum = 0

    for start in range(len(parameter_array)):
        for end in range(start+1, len(parameter_array)+1):
            subarray = parameter_array[start:end]
            for index in range(len(subarray)):
                base = index + 1
                sum += subarray[index] * (base ** i)

    return sum


def generate_parameter_array(N, x1, y1, C, D, E1, E2, F):
    parameters = []

    x = x1
    y = y1
    for i in range(N):
        parameters.append((x + y) % F)

        if i < (N - 1):
            x_next = (C * x + D * y + E1) % F
            y_next = (D * x + C * y + E2) % F
            x, y = x_next, y_next

    return parameters


def test_generate_parameter_array():
    assert generate_parameter_array(1, 0, 1, 1, 1, 1, 1, 3) == [1]
    assert generate_parameter_array(2, 1, 1, 1, 2, 1, 2, 3) == [2, 0]


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N, K, x1, y1, C, D, E1, E2, F = map(int, input().split())

        parameter_array = generate_parameter_array(N, x1, y1, C, D, E1, E2, F)

        power = get_total_power(K, parameter_array)

        print("Case #{}: {}".format(i+1, power % (10**9 + 7)))
