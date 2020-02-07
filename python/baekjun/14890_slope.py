import pytest


def test_check_pass():
    assert check_pass([2, 2, 2, 3, 3, 3], 3) == True
    assert check_pass([3, 2, 2, 1, 2, 3], 1) == False


def check_pass(road, L):
    prev_height = road[0]
    has_slope = [False for _ in range(len(road))]

    def check_slope(i, prev_height, height):
        if abs(prev_height - height) > 1:
            return False

        if prev_height > height:
            for offset in range(L):
                if i + offset >= len(road) or has_slope[i + offset] == True or road[i + offset] != height:
                    return False

                has_slope[i+offset] = True

        if prev_height < height:
            for offset in range(L):
                if i - 1 - offset < 0 or has_slope[i - 1 - offset] == True or road[i - 1 - offset] != prev_height:
                    return False

                has_slope[i-1-offset] = True

        return True

    for i, height in enumerate(road[1:]):
        if prev_height != height:
            if check_slope(i+1, prev_height, height) == False:
                return False
            prev_height = height

    return True


def solution(landscape, N, L):
    count = 0
    for i in range(N):  # check rows
        row = landscape[i]

        if check_pass(row, L):
            count += 1

    for i in range(N):  # check columns
        column = []
        for j in range(N):
            column.append(landscape[j][i])

        if check_pass(column, L):
            count += 1

    return count


if __name__ == '__main__':
    N, L = map(int, input().split(' '))
    landscape = []
    for _ in range(N):
        landscape.append(list(map(int, input().split(' '))))

    print(solution(landscape, N, L))
