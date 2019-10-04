import pytest

import copy

def check_is_valid_bau(jordi_map, x, y):
    if (y > 0 and jordi_map[y-1][x][0]) or (y > 0 and x + 1 < len(jordi_map) and jordi_map[y-1][x+1][0]):
        return True

    if (x > 0 and jordi_map[y][x-1][1]) and (x + 1 < len(jordi_map) and jordi_map[y][x+1][1]):
        return True

    return False


def check_is_valid_column(jordi_map, x, y):
    if y == 0:
        return True

    if y > 0 and jordi_map[y-1][x][0]:
        return True

    if (x > 0 and jordi_map[y][x-1][1]) or jordi_map[y][x][1]:
        return True

    return False


def remove_structure(jordi_map, structure, x, y, a):
    jordi_map[y][x][a] = False

    if a == 0:
        neighbors = [(x, y+1, 0), (x-1, y, 1), (x, y, 1)]

        for ax, ay, aa in neighbors:
            if ax < 0 or ax >= len(jordi_map):
                continue
            
            if ay < 0 or ay >= len(jordi_map):
                continue

            if jordi_map[ay][ax][aa]:
                if aa == 0 and check_is_valid_column(jordi_map, ax, ay) == False:
                    jordi_map[y][x][a] = True
                    return
                if aa == 1 and check_is_valid_bau(jordi_map, ax, ay) == False:
                    jordi_map[y][x][a] = True
                    return
                

    elif a == 1:
        neighbors = [(x, y, 0), (x+1, y, 0), (x-1, y, 1), (x+1, y, 1)]

        for ax, ay, aa in neighbors:
            if ax < 0 or ax >= len(jordi_map):
                continue

            if ay < 0 or ay >= len(jordi_map):
                continue

            if jordi_map[ay][ax][aa]:
                if aa == 0 and check_is_valid_column(jordi_map, ax, ay) == False:
                    jordi_map[y][x][a] = True
                    return
                if aa == 1 and check_is_valid_bau(jordi_map, ax, ay) == False:
                    jordi_map[y][x][a] = True
                    return

    structure.remove([x, y, a])


def build_frame(n, instructions):
    structure = []
    jordi_map = [[[False, False] for _ in range(n+1)] for _ in range(n+1)]

    for x, y, a, b in instructions:
        structure_type = a
        selection = 'Delete' if b == 0 else 'Install'

        if selection == 'Install':
            if structure_type == 0:  # 기둥
                if check_is_valid_column(jordi_map, x, y):
                    structure.append([x, y, a])
                    jordi_map[y][x][0] = True

            else:
                if check_is_valid_bau(jordi_map, x, y):
                    structure.append([x, y, a])
                    jordi_map[y][x][1] = True

        elif selection == 'Delete':
            remove_structure(
                jordi_map, structure, x, y, a)

    structure.sort(key=lambda x: x[2])
    structure.sort(key=lambda x: x[1])
    structure.sort(key=lambda x: x[0])

    return structure


def test_build_frame():
    assert build_frame(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [
                       5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]) == [[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1], [3, 2, 1], [4, 2, 1], [5, 0, 0], [5, 1, 0]]

    assert len(build_frame(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [
        1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]])) == len([[0, 0, 0], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 0, 0]])
