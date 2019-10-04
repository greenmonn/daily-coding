import pytest


def test_4_3():
    building = [
        list('####'),
        list('#*@.'),
        list('####')
    ]

    time = solve(building, 4, 3, (1, 2), [(1, 1)])

    assert time == 2


def test_7_11():
    building = [
        ['#', '#', '#', '.', '#', '#', '#'],
        ['#', '*', '#', '.', '#', '*', '#'],
        ['#', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '.', '@', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#']
    ]
    man_pos = (4, 3)
    fire_poses = [(1, 1), (1, 5)]

    time = solve(building, 7, 11, (9, 3), [(1, 1), (1, 5)])

    assert time == -1


def solve(building, w, h, man_position, fire_positions):
    # 2. 1 iteration ->
        # A. fire expands
        # B. man moves to the all possible positions
            # if cannot move anymore -> impossible
            # if current position is 'outside' -> return t

    t = 0
    man_positions = [man_position]
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False]*w for _ in range(h)]
    visited[man_position[0]][man_position[1]] = True

    def get_possible_moves(pos, skip_visited=True):
        possible_moves = []
        escape_moves = []
        for d in deltas:
            next_pos = (pos[0]+d[0], pos[1]+d[1])

            if next_pos[0] >= h or next_pos[0] < 0 \
                or next_pos[1] >= w or next_pos[1] < 0:
                escape_moves.append(next_pos)
                continue

            if building[next_pos[0]][next_pos[1]] != '.':
                continue

            if skip_visited and visited[next_pos[0]][next_pos[1]] == True:
                continue

            visited[next_pos[0]][next_pos[1]] = True
            possible_moves.append(next_pos)

        return possible_moves, escape_moves

    while True:
        next_fire_positions = []
        for pos in fire_positions:
            # fire expands to possible directions
            possible_moves, _ = get_possible_moves(pos, skip_visited=False)

            for p in possible_moves:
                building[p[0]][p[1]] = '*'
                next_fire_positions.append(p)

        next_man_positions = []
        for pos in man_positions:
            # man moves to possible directions

            possible_moves, escape_moves = get_possible_moves(pos)

            if len(escape_moves) > 0:
                return t + 1

            for p in possible_moves:
                next_man_positions.append(p)

        if len(next_man_positions) == 0:
            return -1

        man_positions = next_man_positions
        fire_positions = next_fire_positions

        t += 1


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        w, h = map(int, input().split(' '))
        building = []

        man_position = (None, None)
        fire_positions = []

        for i in range(h):
            line = list(input())

            for j, c in enumerate(line):
                if c == '@':
                    man_position = (i, j)
                if c == '*':
                    fire_positions.append((i, j))

            building.append(line)

        ans = solve(building, w, h, man_position, fire_positions)

        if ans == -1:
            ans = 'IMPOSSIBLE'

        print(ans)
