from enum import IntEnum
import copy


class Tunnel(IntEnum):
    CROSS = 1
    VERTICAL = 2
    HORIZONTAL = 3
    TOP_RIGHT = 4
    BOTTOM_RIGHT = 5
    BOTTOM_LEFT = 6
    TOP_LEFT = 7


def has_top_entry(type):
    return type == Tunnel.CROSS or type == Tunnel.VERTICAL \
           or type == Tunnel.TOP_RIGHT or type == Tunnel.TOP_LEFT


def has_bottom_entry(type):
    return type == Tunnel.CROSS or type == Tunnel.VERTICAL \
           or type == Tunnel.BOTTOM_RIGHT or type == Tunnel.BOTTOM_LEFT


def has_left_entry(type):
    return type == Tunnel.CROSS or type == Tunnel.HORIZONTAL \
           or type == Tunnel.TOP_LEFT or type == Tunnel.BOTTOM_LEFT


def has_right_entry(type):
    return type == Tunnel.CROSS or type == Tunnel.HORIZONTAL \
           or type == Tunnel.TOP_RIGHT or type == Tunnel.BOTTOM_RIGHT


def get_next_positions(pos, tunnel_map, rows, cols, visited):
    next_positions = []

    y, x = pos
    type = tunnel_map[y][x]
    if has_top_entry(type):
        if y > 0 and has_bottom_entry(tunnel_map[y - 1][x]) and (y - 1, x) not in visited:
            next_positions.append((y - 1, x))
            visited.append((y - 1, x))

    if has_bottom_entry(type):
        if y < rows - 1 and has_top_entry(tunnel_map[y + 1][x]) and (y + 1, x) not in visited:
            next_positions.append((y + 1, x))
            visited.append((y + 1, x))

    if has_left_entry(type):
        if x > 0 and has_right_entry(tunnel_map[y][x - 1]) and (y, x - 1) not in visited:
            next_positions.append((y, x - 1))
            visited.append((y, x - 1))

    if has_right_entry(type):
        if x < cols - 1 and has_left_entry(tunnel_map[y][x + 1]) and (y, x + 1) not in visited:
            next_positions.append((y, x + 1))
            visited.append((y, x + 1))

    return next_positions


def get_criminal_positions(manhole, time, tunnel_map, rows, cols):
    candidate_positions = [manhole]

    visited = [manhole]

    for t in range(time - 1):
        next_positions = []
        for pos in candidate_positions:
            next_positions.extend(get_next_positions(pos, tunnel_map, rows, cols, visited))

        candidate_positions = next_positions[:]

    return visited


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N, M, R, C, L = map(int, input().split(' '))

        tunnel_map = []
        for j in range(N):
            tunnel_map.append(list(map(int, input().split(' '))))

        manhole = (R, C)
        time = L

        locations = get_criminal_positions(manhole, time, tunnel_map, N, M)

        print('#{} {}'.format(i + 1, len(locations)))
