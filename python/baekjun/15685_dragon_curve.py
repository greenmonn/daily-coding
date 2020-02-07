
directions = {
    0: (0, 1),
    1: (-1, 0),
    2: (0, -1),
    3: (1, 0)
}


def draw_curve(grid, x, y, d, g):
    dy, dx = directions[d]
    start_vertex = (x, y)
    vertices = [(x, y), (x+dx, y+dy)]
    end_vertex = (x+dx, y+dy)
    grid[y][x] = 1
    grid[y+dy][x+dx] = 1

    for i in range(g):
        x, y = end_vertex
        new_vertices = vertices[:]
        for v in vertices:
            a, b = v
            c, d = x+y-b, a-x+y
            new_vertices.append((c, d))
            grid[d][c] = 1

        a, b = start_vertex
        end_vertex = (x+y-b, a-x+y)
        vertices = new_vertices


def solution(dragon_curves, N):
    grid = [[0] * 101 for _ in range(101)]
    # draw all dragon curves and mark vertices
    for curve in dragon_curves:
        x, y, d, g = curve

        draw_curve(grid, x, y, d, g)

    def has_all_vertices_from_curve(vertices):
        for x, y in vertices:
            if grid[y][x] != 1:
                return False
        return True

    # iterate all squares and check vertices
    count = 0
    for i in range(100):
        for j in range(100):
            vertices = [(i, j), (i, j+1), (i+1, j), (i+1, j+1)]

            if has_all_vertices_from_curve(vertices):
                count += 1

    return count


if __name__ == '__main__':
    N = int(input())

    dragon_curves = []
    for i in range(N):
        x, y, d, g = map(int, input().split(' '))
        dragon_curves.append((x, y, d, g))

    print(solution(dragon_curves, N))
