directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def is_ok(i, j):
    if i < 0 or i >= R:
        return False

    if j < 0 or j >= C:
        return False

    if room[i][j] == -1:
        return False

    return True


def is_valid(room, i, j):
    if i < 0 or i >= R:
        return False

    if j < 0 or j >= C:
        return False

    return True


def spread(room, R, C):
    prev_room = [[n for n in row] for row in room]

    for i in range(R):
        for j in range(C):
            if prev_room[i][j] <= 0:
                continue

            loss = 0
            for di, dj in directions:
                if is_ok(i+di, j+dj):
                    room[i+di][j+dj] += prev_room[i][j]//5
                    loss += prev_room[i][j]//5

            # 자신의 미세먼지의 양 업데이트
            room[i][j] -= loss


def step(room, cleaner_pos, R, C):
    spread(room, R, C)

    def blow_wind(cleaner_pos, directions):
        d = 0
        di, dj = directions[d]
        pos = (cleaner_pos[0]+di, cleaner_pos[1]+dj)

        prev_value = 0

        while pos != cleaner_pos:
            i, j = pos
            di, dj = directions[d]
            if is_valid(room, i+di, j+dj):
                pos = i+di, j+dj
            else:
                d = (d+1) % 4
                di, dj = directions[d]
                pos = i+di, j+dj

            temp = room[i][j]
            room[i][j] = prev_value
            prev_value = temp

    blow_wind(cleaner_pos[0], [(0, 1), (-1, 0), (0, -1), (1, 0)])
    blow_wind(cleaner_pos[1], [(0, 1), (1, 0), (0, -1), (-1, 0)])


def solution(room, cleaner_pos, R, C, T):
    # for time T
    for t in range(T):
        step(room, cleaner_pos, R, C)

    sum = 0
    for i in range(R):
        for j in range(C):
            if room[i][j] != -1:
                sum += room[i][j]
    return sum


if __name__ == '__main__':
    R, C, T = map(int, input().split(' '))

    room = []
    cleaner_pos = []
    for i in range(R):
        row = list(map(int, input().split(' ')))
        for j in range(C):
            if row[j] == -1:
                cleaner_pos.append((i, j))
        room.append(row)
    print(solution(room, cleaner_pos, R, C, T))
