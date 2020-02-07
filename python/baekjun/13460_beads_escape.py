# Again: Incorrect

import copy
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def can_move(board, i, j, di, dj, visited, N, M):
    r, c = i+di, j+dj

    if r < 0 or r >= N:
        return False

    if c < 0 or c >= M:
        return False

    if board[r][c] == '#':
        return False

    if board[r][c] == 'B' or board[r][c] == 'R':
        return can_move(board, r, c, di, dj, visited, N, M)

    if visited[r][c] == True:
        return False

    visited[r][c] = True
    return True


def solution(board, red_pos, blue_pos, N, M):
    red_pos = [red_pos]
    blue_pos = [blue_pos]
    r_visited = [[[False for _ in range(M)] for _ in range(N)]]
    b_visited = [[[False for _ in range(M)] for _ in range(N)]]

    for t in range(10):
        next_red_pos = []
        next_blue_pos = []
        next_r_visited = []
        next_b_visited = []

        if len(red_pos) == 0:
            return -1

        for x, pos in enumerate(red_pos):
            i, j = pos
            r, c = blue_pos[x]
            print(pos)
            print(blue_pos[x])
            print('\n')
            b_visited_ = copy.deepcopy(b_visited[x])
            r_visited_ = copy.deepcopy(r_visited[x])
            if board[r][c] == 'O':
                return -1
            if board[i][j] == 'O':
                return t

            for d in range(4):
                di, dj = directions[d]
                has_move = False

                new_blue_pos = (r, c)
                if can_move(board, r, c, di, dj, b_visited_, N, M):
                    new_blue_pos = (r+di, c+dj)
                    has_move = True

                if can_move(board, i, j, di, dj, r_visited_, N, M):
                    next_red_pos.append((i+di, j+dj))
                    next_blue_pos.append(new_blue_pos)
                    next_r_visited.append(r_visited_)
                    next_b_visited.append(b_visited_)

                elif has_move == True:
                    next_red_pos.append((i, j))
                    next_blue_pos.append(new_blue_pos)
                    next_r_visited.append(r_visited_)
                    next_b_visited.append(b_visited_)

        red_pos = next_red_pos
        blue_pos = next_blue_pos
        b_visited = next_b_visited
        r_visited = next_r_visited

    return -1


if __name__ == '__main__':
    N, M = map(int, input().split(' '))

    board = []
    red_pos = None
    blue_pos = None
    for i in range(N):
        row = list(input())
        for j, c in enumerate(row):
            if c == 'B':
                blue_pos = (i, j)
            elif c == 'R':
                red_pos = (i, j)

        board.append(row)

    print(solution(board, red_pos, blue_pos, N, M))
