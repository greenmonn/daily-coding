def tour_cafes(cafe_map, N):
    # 경로 중에 같은 숫자가 한 번도 포함되면 안됨
    # 이미 갔던 곳 다시가면 안됨
    # 대각선으로만 가야함
    # 반만 그리면 나머지 경로가 결정됨 (평행사변형)

    max_length = 0

    for y in range(N):
        for x in range(N):
            if not ((y == 0 and x == 0) or (y==0 and x == N-1) or (y== N-1 and x ==0 ) or (y == N-1 and x == N-1)):
                route = find_longest_route((y, x), cafe_map, N)
                if len(route) > max_length:
                    max_length = len(route)

    return max_length


def is_in_the_map(pos, N):
    return 0 < pos[0] < N and 0 < pos[1] < N


def find_longest_route(start_pos, cafe_map, N):




if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        N = int(input())

        cafe_map = []
        for j in range(N):
            row = list(map(int, input().split(' ')))
            cafe_map.append(row)

        route = tour_cafes(cafe_map, N)

        print('#{} {}'.format(i + 1, len(route)))
