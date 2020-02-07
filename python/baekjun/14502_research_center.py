import pytest
import itertools
import copy


def test_num_of_safe_zones():
    room = [[2, 1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 2, 0], [0, 1, 1, 0, 1, 0, 0], [
        0, 1, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]]

    viruses = [(0, 0), (1, 5)]

    assert 27 == get_num_of_safe_zones(room, viruses)


def get_num_of_safe_zones(room, viruses):
    to_visits = viruses[:]

    deltas = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def is_ok(pos):
        if pos[0] < 0 or pos[0] >= len(room):
            return False

        if pos[1] < 0 or pos[1] >= len(room[0]):
            return False

        if room[pos[0]][pos[1]] != 0:
            return False

        return True

    while len(to_visits) > 0:
        next_visits = []
        for pos in to_visits:
            for di, dj in deltas:
                next_pos = (pos[0]+di, pos[1]+dj)
                if is_ok(next_pos):
                    room[next_pos[0]][next_pos[1]] = 2
                    next_visits.append(next_pos)

        to_visits = next_visits

    num_of_safe_zones = 0
    for i in range(len(room)):
        for j in range(len(room[i])):
            if room[i][j] == 0:
                num_of_safe_zones += 1

    return num_of_safe_zones


def solution(room, viruses, empty_locs, walls, M, N):
    max_num_of_safe_zones = 0

    new_wall_candidates = itertools.combinations(empty_locs, 3)

    for new_walls in new_wall_candidates:
        new_room = copy.deepcopy(room)

        for i, j in new_walls:
            new_room[i][j] = 1

        num_of_safe_zones = get_num_of_safe_zones(new_room, viruses)

        if num_of_safe_zones > max_num_of_safe_zones:
            max_num_of_safe_zones = num_of_safe_zones

    return max_num_of_safe_zones


if __name__ == '__main__':
    N, M = map(int, input().split(' '))

    room = []
    viruses = []
    empty_locs = []
    walls = []

    for i in range(N):
        row = list(map(int, input().split(' ')))
        for j, num in enumerate(row):
            if num == 0:
                empty_locs.append((i, j))
            elif num == 1:
                walls.append((i, j))
            elif num == 2:
                viruses.append((i, j))

        room.append(row)

    print(solution(room, viruses, empty_locs, walls, M, N))
