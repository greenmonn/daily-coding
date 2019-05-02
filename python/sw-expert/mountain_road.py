def build_road(N, maxCutDepth, mountain):
    highest_points = get_highest_points(N, mountain)

    max_length = 0
    for point in highest_points:
        length = build_road_from(point, N, maxCutDepth, 1, mountain)
        if length > max_length:
            max_length = length

    return max_length


def clone(mountain):
    new_map = []
    for row in mountain:
        new_map.append(row[:])

    return new_map


def build_road_from(point, N, maxCutDepth, cut_count, mountain):
    y, x = point
    height = mountain[y][x]
    mountain = clone(mountain)
    mountain[y][x] = 21

    neighbors = []
    if x > 0:
        neighbors.append((y, x - 1))
    if x < N - 1:
        neighbors.append((y, x + 1))
    if y > 0:
        neighbors.append((y - 1, x))
    if y < N - 1:
        neighbors.append((y + 1, x))

    candidate_lengths = []
    for neighbor in neighbors:
        y, x = neighbor
        if mountain[y][x] < height:
            length = 1 + build_road_from(neighbor, N, maxCutDepth, cut_count, mountain)
            candidate_lengths.append(length)

        elif cut_count > 0 and mountain[y][x] - maxCutDepth < height:
            mountain = clone(mountain)
            mountain[y][x] = height - 1
            length = 1 + build_road_from(neighbor, N, maxCutDepth, cut_count - 1, mountain)
            candidate_lengths.append(length)

    if len(candidate_lengths) == 0:
        return 1

    return max(candidate_lengths)


def get_highest_points(N, mountain):
    highest_points = []
    highest = 0
    for row in range(N):
        for col in range(N):
            if mountain[row][col] > highest:
                highest = mountain[row][col]
                highest_points = [(row, col)]
            elif mountain[row][col] == highest:
                highest_points.append((row, col))

    return highest_points


if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        N, maxCutDepth = map(int, input().split(' '))

        mountain = []

        for j in range(N):
            row = list(map(int, input().split(' ')))
            mountain.append(row)

        max_length = build_road(N, maxCutDepth, mountain)
        print('#{} {}'.format(i + 1, max_length))
