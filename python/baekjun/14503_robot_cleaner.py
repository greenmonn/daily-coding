import pytest

directions = {
    0: (-1, 0),  # 북
    1: (0, 1),  # 동
    2: (1, 0),  # 남
    3: (0, -1)  # 서
}


def test_clean():
    room = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    start_pos = (1, 1)
    d = 0

    assert solution(room, start_pos, d) == 1


def solution(room, start_pos, d):

    def is_ok(i, j):
        if i < 0 or i > len(room):
            return False

        if j < 0 or j > len(room[0]):
            return False

        if room[i][j] != 0:
            return False

        return True

    def is_not_wall(i, j):
        if i < 0 or i > len(room):
            return False

        if j < 0 or j > len(room[0]):
            return False

        if room[i][j] == 1:
            return False

        return True

    num_cleaned = 0

    while True:
        i, j = start_pos
        if room[i][j] == 0:
            room[i][j] = 2
            num_cleaned += 1

        advance = False
        for _ in range(4):
            d = (d - 1 + 4) % 4
            di, dj = directions[d]

            if is_ok(i+di, j+dj):
                i, j = i+di, j+dj
                advance = True
                break

        if advance == False:
            di, dj = directions[d]
            if is_not_wall(i-di, j-dj):
                i, j = i-di, j-dj
            else:
                return num_cleaned

        start_pos = i, j

    return 0


if __name__ == '__main__':
    N, M = map(int, input().split(' '))
    r, c, d = map(int, input().split(' '))
    room = []

    for i in range(N):
        row = list(map(int, input().split(' ')))
        room.append(row)

    print(solution(room, (r, c), d))
