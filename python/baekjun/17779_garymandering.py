import unittest


class TestSolution(unittest.TestCase):
    def test_sample(self):
        pass

def divide_city(city, i, j, d1, d2, N):
    sums = [0] * 5
    for r in range(N):
        for c in range(N):
            if 1 <= r < i and 1 <= c < j+d1:
                sums[0] += city[r][c]
            elif i < r < N and 1 <= c <= j+d2:
                sums[1] += city[r][c]
            elif j + d1 <= c < N and 1 <= r < i-d1+d2:
                sums[2] += city[r][c]
def solution(city, N):
    min_diff = 10**10

    for j in range(N-2):
        for i in range(1, N-1):
            point = (i, j)

            for d1 in range(1, N - j):
                for d2 in range(1, min(i, N-1-i)+1):
                    if d1 + d2 > N - 1 - j:
                        continue

                    diff = divide_city(city, i, j, d1, d2, N)
                    if diff < min_diff:
                        min_diff = diff

    return min_diff


if __name__ == '__main__':
    N = int(input())

    city = []
    for i in range(N):
        row = list(map(int, input().split(' ')))
        city.append(row)

    print(solution(city, N))
