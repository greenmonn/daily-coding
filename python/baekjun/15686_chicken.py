import itertools


def distance(x, y):
    a, b = x
    c, d = y

    return abs(a-c) + abs(b-d)


def dist(chickens, homes, N):
    dist_sum = 0
    for home in homes:
        chicken_dist = 10**10
        for chicken in chickens:
            d = distance(home, chicken)
            if d < chicken_dist:
                chicken_dist = d

        dist_sum += chicken_dist

    return dist_sum


def solution(city, homes, chickens, N, M):
    selected_chicken_candidates = itertools.combinations(chickens, M)

    min_d = 10**10
    for selected in selected_chicken_candidates:
        d = dist(selected, homes, N)
        if d < min_d:
            min_d = d

    return min_d


if __name__ == '__main__':
    N, M = map(int, input().split(' '))

    city = []
    homes = []
    chickens = []
    for i in range(N):
        row = list(map(int, input().split(' ')))
        for j, n in enumerate(row):
            if n == 1:
                homes.append((i, j))
            elif n == 2:
                chickens.append((i, j))
        city.append(row)

    print(solution(city, homes, chickens, N, M))
