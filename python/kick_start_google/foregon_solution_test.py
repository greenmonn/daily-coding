import pytest


def has_digit_of_4(number):
    return has_digit_of_4_on(number, 0)

def has_digit_of_4_on(number, pos):
    if number % 10 == 4:
        return (True, pos)
    if number // 10 == 0:
        return (False, -1)

    return has_digit_of_4_on(number // 10, pos + 1)


def test_has_digit_of_4():
    assert (True, 0) == has_digit_of_4(4)
    assert (False, -1) == has_digit_of_4(852)
    assert (True, 1) == has_digit_of_4(40)
    assert (True, 2) == has_digit_of_4(470)


def find_two_checks(N):
    A = N // 2
    B = N - A

    while (True):
      has_digit_of_4_A, pos_A = has_digit_of_4(A)
      has_digit_of_4_B, pos_B = has_digit_of_4(B)
      if not (has_digit_of_4_A or has_digit_of_4_B):
        break
      
      A += 10 ** max(pos_A, pos_B)
      B = (N - A)

    return [A, B]


def test_find_two_checks():
    assert [2, 2] == find_two_checks(4)
    assert [570, 370] == find_two_checks(940)


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())

        A, B = find_two_checks(N)

        print("Case #{}: {} {}".format(i+1, A, B))
